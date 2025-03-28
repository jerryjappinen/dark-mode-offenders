# pylint: disable=missing-function-docstring
"""Some basic unit tests."""

import datetime
from utils import normalize_updates_input_item, app_to_md_row, group_by, map_dict, format_date

def test_all():
    test_normalize_updates_input_item()
    test_app_to_md_row()
    test_group_by()
    test_map_dict()
    test_format_date()



# normalize
def test_normalize_updates_input_item():
    res = normalize_updates_input_item({
        "date": "2021-01-03",
        "description": "    Spotify light mode released."
    })
    assert res == {
        "date": datetime.datetime(2021, 1, 3),
        "description": "Spotify light mode released."
    }



# app_to_md_row

def test_app_to_md_row():
    app = {
        "name": "App 1",
        "references": ["https://example.com"],
        "web": "done",
        "mobile": "no_release",
        "desktop": "unknown",
        "url": None,
        "is_done": False
    }

    res = app_to_md_row(app)
    assert res == "|App 1 ([1](https://example.com))|✅|-|?|"



# Utils

def test_group_by():
    res = group_by([
        {"group": "A", "name": "App 1"},
        {"group": "B", "name": "App 2"},
        {"group": "A", "name": "App 3"}
    ], "group")

    assert res == {
        "A": [
            {"group": "A", "name": "App 1"},
            {"group": "A", "name": "App 3"}
        ],
        "B": [
            {"group": "B", "name": "App 2"}
        ]
    }

def test_map_dict():
    res = map_dict(lambda x: x.upper(), {
        "a": "a",
        "b": "b",
        "c": "c"
    })
    assert res == {
        "a": "A",
        "b": "B",
        "c": "C"
    }

def test_format_date():
    res = format_date(datetime.datetime(2021, 1, 3))
    assert res == "Jan 03, 2021"

if __name__ == "__main__":
    test_all()
    print("✔️ All tests passed")
