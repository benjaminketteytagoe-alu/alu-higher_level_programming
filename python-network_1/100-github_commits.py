import requests
import sys

def get_commits(repo, owner):
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
,benjaminketteytagoe-alu)
