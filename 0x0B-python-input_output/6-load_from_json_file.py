#!/usr/bin/python3
"""load from json"""
import json


def load_from_json_file(fname):
    """load from json to file"""
    with open(fname, encoding="utf-8") as file_loaded:
        return json.load(file+loaded)
