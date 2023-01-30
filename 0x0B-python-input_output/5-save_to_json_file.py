#!/usr/bin/python3
"""write obj to .txt using json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a json rep"""

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
