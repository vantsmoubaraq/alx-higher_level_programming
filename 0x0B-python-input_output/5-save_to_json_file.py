#!usr/bin/python3

"""
function that writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    text = json.dumps(my_obj)

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
