#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://100.26.246.254/search_user"
    if len(argv) == 2:
        value = {"q": argv[2]}
    else:
        value = {"q": ""}

    response = requests.post(url, data=value)

    try:
        j_res = response.json()

        for key, value in j_res.items():
            print(f"{[key]} {value}")
    except Exception as e:
        if response.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
