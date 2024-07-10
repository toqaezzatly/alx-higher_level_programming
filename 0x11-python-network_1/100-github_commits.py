#!/usr/bin/python3
"""
This module takes in a repository name and an owner name, uses the GitHub API
to list the 10 most recent commits, and prints each commit's SHA and author name.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    
    commits = response.json()
    
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")

