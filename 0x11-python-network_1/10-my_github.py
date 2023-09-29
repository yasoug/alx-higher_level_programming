#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(f"{url}{username}",
                            headers={"Authorization": f"token {password}"},
                            )
    print(response.json().get("id"))
