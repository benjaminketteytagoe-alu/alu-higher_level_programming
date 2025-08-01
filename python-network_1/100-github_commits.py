#!/usr/bin/python3
"""
Module: 100-github_commits.py

This script retrieves and displays the 10 most recent commits of a specified
GitHub repository using the GitHub API. It takes two command-line arguments:
the repository name and the owner name. The commits are printed in the format
`<sha>: <author name>`, one per line.
"""

import requests
import sys


def get_commits(alu-higher_level_programming
, benjaminketteytagoe-alu):
    """
    Fetches the 10 most recent commits from a GitHub repository.

    Args:
        repo (str): The name of the repository.
        owner (str): The username of the repository owner.

    Prints:
        For each commit, the SHA and the author's name in the format:
        `<sha>: <author name>`.

    Note:
        Uses the GitHub API endpoint for commits with a limit of 10 commits per page.
        Handles unauthenticated requests, which are subject to GitHub's rate limit
        of 60 requests per hour per IP.
    """
    url = f"https://api.github.com/repos/benjaminketteytagoe-alu/alu-higher_level_programming
/commits"
    params = {"per_page": 10}
    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(alu-higher_level_programming
, benjaminketteytagoe-alu)
