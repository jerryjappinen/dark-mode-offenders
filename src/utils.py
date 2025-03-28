# pylint: disable=missing-function-docstring
"""Code for managing data and building the README."""

import csv
import json

from datetime import datetime
from config import csv_delimiter, default_group, platforms, verdicts

verdicts_reverse = dict((v,k) for k,v in verdicts.items())
verdict_keys = list(verdicts.keys())



# Main routine

def build_files(
        apps_csv_path,
        updates_csv_path,
        json_path,
        base_readme_path,
        target_readme_path
    ):

    apps_input, updates_input = load_data_from_csv(apps_csv_path, updates_csv_path)
    apps = normalize_apps_input(apps_input)
    updates = normalize_updates_input(updates_input)
    stats = apps_to_stats(apps)

    write_data_to_json(json_path, apps, updates, stats)

    new_readme = generate_readme(apps, updates, base_readme_path)
    write_to_readme(target_readme_path, new_readme)



# File ops

def write_apps_to_csv(target_csv_path, apps):
    with open(target_csv_path, "w", encoding = "utf-8") as f:
        f.write(apps_to_csv(apps))

def write_data_to_json(target_json_path, apps, updates, stats):
    content = data_to_json(apps, updates, stats)
    with open(target_json_path, "w", encoding = "utf-8") as f:
        f.write(content)

def write_to_readme(target_readme_path, updated_readme):
    with open(target_readme_path, "w", encoding = "utf-8") as f:
        f.write(updated_readme)

def load_data_from_csv(apps_data_path, updates_data_path):

    # Load apps from CSV
    with open(apps_data_path, encoding = "utf-8", newline = "") as f:
        dict_reader = csv.DictReader(f, delimiter = csv_delimiter)
        apps_input = list(dict_reader)

    # Load updates from CSV
    with open(updates_data_path, encoding = "utf-8", newline = "") as f:
        dict_reader = csv.DictReader(f, delimiter = csv_delimiter)
        updates_input = list(dict_reader)

    return (apps_input, updates_input)

def load_data_from_json(data_path):
    with open(data_path, "r", encoding = "utf-8") as f:
        data = json.load(f)
        apps_input = data["apps"]
        updates_input = data["updates"]
    return (apps_input, updates_input)

def generate_readme(apps, updates, base_readme_path):
    # stats_output = stats_to_md_table(stats)
    apps_output = apps_to_grouped_md_table(apps)
    updates_output = updates_to_md_list(updates)

    # Replace the placeholder in the README base
    with open(base_readme_path, "r", encoding = "utf-8") as f:
        readme_base = f.read()

    return (
        readme_base
            .strip()
            .replace("{ apps_output }", apps_output)
            .replace("{ updates_output }", updates_output)
    ) + "\n"



# Check and fix input CSV/JSON

def normalize_apps_input(input_list):
    apps = map(normalize_apps_input_item, input_list)
    return sorted(apps, key = lambda a: a["name"].lower())

def normalize_apps_input_item(obj):
    name = obj["name"].strip() if "name" in obj else None
    web = obj["web"] if "web" in obj else None
    mobile = obj["mobile"] if "mobile" in obj else None
    desktop = obj["desktop"] if "desktop" in obj else None
    url = obj["url"].strip() if "url" in obj else None
    group = obj["group"] if "group" in obj else default_group
    references = obj["references"] if "references" in obj else None

    if not references:
        references = []
    elif isinstance(references, str):
        references = list(map(lambda s: s.strip(), references.split(";")))
    elif not isinstance(references, list):
        references = [references]

    if not name:
        raise ValueError("Name is missing")

    if not (web and mobile and desktop):
        raise ValueError("Missing verdicts (must have web, mobile and desktop.")

    if not (web in verdict_keys and mobile in verdict_keys and desktop in verdict_keys):
        verdict_keys_string = ", ".join(verdict_keys)
        raise ValueError(f"Only these verdicts are allowed: { verdict_keys_string }.")

    is_done = True
    for val in [web, mobile, desktop]:
        if val not in ["done", "no_release"]:
            is_done = False
            break

    return {
        "name": name,
        "web": web,
        "mobile": mobile,
        "desktop": desktop,
        "url": url,
        "group": group,
        "references": references,
        "is_done": is_done
    }

def normalize_updates_input(input_list):
    updates = map(normalize_updates_input_item, input_list)
    return sorted(updates, key = lambda u: u["date"])

def normalize_updates_input_item(obj):
    d = obj["date"].strip() if "date" in obj else None
    description = obj["description"].strip() if "description" in obj else None

    if not (d and description):
        raise ValueError("Each update should have a date and a description")

    return {
        "date": datetime.fromisoformat(d),
        "description": description
    }



# Converting between data to/from CSV

def apps_to_stats(apps):
    total = len(apps)
    is_done_count = len(list(filter(lambda a: a["is_done"], apps)))

    res = {
        "total": total,
        "is_done": is_done_count,
        "groups": map_dict(len, group_by(apps, "group")),
        "status": {}
    }

    for platform in platforms:
        res["status"][platform] = map_dict(len, group_by(apps, platform))
        res["status"][platform]["total"] = total - res["status"][platform]["no_release"]

        for verdict in verdict_keys:
            if not verdict in res["status"][platform]:
                res["status"][platform][verdict] = 0

    return res

def apps_to_csv(apps):
    return csv_delimiter.join([
        "group",
        "name",
        "web",
        "mobile",
        "desktop",
        "url",
        "references"
    ]) + "\n" + "\n".join(list(map(
        lambda a: csv_delimiter.join([
            a["group"],
            a["name"],
            a["web"],
            a["mobile"],
            a["desktop"],
            a["url"] if a["url"] else "",
            "; ".join(a["references"]) if "references" in a else ""
        ]),
        apps
    )))



# Converting between data to/from Markdown

def data_to_json (apps, updates, stats):
    res = {
        "stats": stats,
        "apps": list(map(app_to_json, apps)),
        "updates": list(map(update_to_json, updates))
    }

    return json.dumps(res, indent = 2)

def app_to_json(app):
    a = app.copy()
    if not a["url"]:
        del a["url"]
    if not a["references"]:
        del a["references"]
    return a

def update_to_json(update):
    return {
        "date": update["date"].strftime("%Y-%m-%d"),
        "description": update["description"]
    }

def updates_to_md_list (updates):
    return "\n".join(map(lambda u: f"- { format_date(u['date']) }: { u['description'] }", updates))

def apps_to_grouped_md_table (apps):
    apps_by_group = group_by(apps, "group")
    group_names = sorted(apps_by_group.keys())
    if default_group in group_names:
        group_names.remove(default_group)
        group_names.insert(0, default_group)

    md = ""
    for i, group_name in enumerate(group_names):
        if i:
            md += f"### { group_name }" + "\n\n"
        md += apps_to_md_table(apps_by_group[group_name]) + "\n\n"

    return md.strip()

def apps_to_md_table (apps):
    table_rows = "\n".join(map(app_to_md_row, apps))
    return f"""|App<img width=220 />|Web|Mobile app|Desktop app|
|:-|:-:|:-:|:-:|
{ table_rows }"""

def app_to_md_row (app):
    n = app["name"]
    u = app["url"]

    name_cell = f"[{ n }]({ u })" if u else n

    # Strikeout for completed apps
    if app["is_done"]:
        name_cell = f"~~{ name_cell }~~ *"

    # This creates ([1](https://...), [2](https://...))
    elif len(app["references"]):
        references = list(map(
            lambda kv: f"[{ kv[0] + 1 }]({ kv[1] })",
            enumerate(app["references"])
        ))
        references_string = ", ".join(references)
        name_cell += f" ({ references_string })"

    a = verdicts[app["web"]]
    m = verdicts[app["mobile"]]
    d = verdicts[app["desktop"]]

    return f"|{ name_cell }|{ a }|{ m }|{ d }|"

def md_row_to_app_input(row):
    name_with_url = row[0].strip()
    name_with_url_components = name_with_url.split("](")

    name = name_with_url
    url = ""
    web = verdicts_reverse[row[1].strip()]
    mobile = verdicts_reverse[row[2].strip()]
    desktop = verdicts_reverse[row[3].strip()]

    name = name_with_url
    if len(name_with_url_components) > 1:
        name = name_with_url_components[0].strip("[")
        url = name_with_url_components[1].strip(")")

    res = {
        "name": name,
        "url": url,
        "web": web,
        "mobile": mobile,
        "desktop": desktop
    }

    return res



# Utils

def group_by (data_as_list, key):
    res = {}
    for item in data_as_list:
        if item[key] not in res:
            res[item[key]] = []
        res[item[key]].append(item)
    return res

def map_dict (callback, dict_to_map):
    return dict(map(lambda kv: (kv[0], callback(kv[1])), dict_to_map.items()))

# https://stackoverflow.com/questions/46318714/how-do-i-generate-a-python-timestamp-to-a-particular-format
def format_date (timestamp):
    return timestamp.strftime("%b %d, %Y")
