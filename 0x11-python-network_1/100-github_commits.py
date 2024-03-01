#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
