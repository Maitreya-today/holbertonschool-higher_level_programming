#!/usr/bin/python3
"""json rep (object)"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    rep by a json string"""

    return json.loads(my_str)
