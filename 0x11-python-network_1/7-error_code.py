#!/usr/bin/python3
"""
takes in a URL,sends a request to the URL
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
