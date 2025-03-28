# pylint: disable=missing-function-docstring
"""Code for managing data and building the README."""

import json
from config import default_group, verdicts

verdicts_reverse = dict((v,k) for k,v in verdicts.items())
verdict_keys = list(verdicts.keys())


# Main routines

def write_to_readme(target_readme_path, updated_readme):
    with open(target_readme_path, "w", encoding = "utf-8") as readme_file:
        readme_file.write(updated_readme)

def generate_readme(data_path, base_readme_path):
    with open(data_path, "r", encoding = "utf-8") as f:
        data = json.load(f)
        apps_input = data["apps"]
        updates_input = data["updates"]

    # Generate Markdown output
    apps = normalize_apps_input(apps_input)
    # stats = compose_stats(apps)
    # stats_output = stats_to_md_table(stats)
    apps_output = apps_to_grouped_md_table(apps)
    updates_output = updates_to_md_list(updates_input)

    # Replace the placeholder in the README base
    with open(base_readme_path, "r", encoding = "utf-8") as f:
        readme_base = f.read()

    return (
        readme_base
            .strip()
            .replace("{ apps_output }", apps_output)
            .replace("{ updates_output }", updates_output)
    ) + "\n"



# Check and fix input JSON

def normalize_apps_input(json_list):
    return list(map(normalize_apps_input_obj, json_list))

def normalize_apps_input_obj(obj):
    name = obj["name"].strip() if "name" in obj else None
    web = obj["web"] if "web" in obj else None
    mobile = obj["mobile"] if "mobile" in obj else None
    desktop = obj["desktop"] if "desktop" in obj else None
    url = obj["url"].strip() if "url" in obj else None
    group = obj["group"] if "group" in obj else default_group
    references = obj["references"] if "references" in obj and isinstance([], list) else []

    if not name:
        raise ValueError("Name is missing")

    if not (web and mobile and desktop):
        raise ValueError("Missing verdicts (must have web, mobile and desktop.")

    if not (web in verdict_keys and mobile in verdict_keys and desktop in verdict_keys):
        verdict_keys_string = ", ".join(verdict_keys)
        raise ValueError(f"Only these verdicts are allowed: { verdict_keys_string }.")

    # is_done = True if web + mobile + desktop == "donedonedone" else False
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



# Goodies

def compose_stats(apps):
    return {
        "total": len(apps),
        "groups": map_dict(len, group_by(apps, "group")),
        "web": map_dict(len, group_by(apps, "web")),
        "mobile": map_dict(len, group_by(apps, "mobile")),
        "desktop": map_dict(len, group_by(apps, "desktop"))
    }



# Converting between data to/from Markdown

def updates_to_md_list (updates):
    return "\n".join(map(lambda u: f"- { u }", updates))

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

    return md

def apps_to_md_table (apps):
    table_rows = "\n".join(map(app_to_md_row, apps))
    return f"""|App|Web|Mobile app|Desktop app|
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
