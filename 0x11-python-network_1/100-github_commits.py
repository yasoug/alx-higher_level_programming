#!/usr/bin/python3
"""
Script that takes repo and owner name,
and uses Github API to list last 10 commits
"""
import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo)
    response = requests.get(url)
    list_commits = response.json()
    for commit in list_commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
