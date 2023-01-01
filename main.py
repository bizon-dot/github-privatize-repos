
import requests


TOKEN = "{TOKEN}"

BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"Token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

page = 1

more_pages = True

repositories = []

while more_pages:
    response = requests.get(f"{BASE_URL}/user/repos?page={page}", headers=headers)

    if response.status_code != 200:
        print("Error: Could not get list of repositories.")
        exit(1)

    repos = response.json()

    repositories += repos

    if "next" not in response.links:
        more_pages = False
    else:
        page += 1


for repo in repositories:
    repo_name = repo["name"]
    print(f"Setting {repo_name} to private...")
    response = requests.patch(f"{BASE_URL}/repos/{repo['full_name']}", json={"private": True}, headers=headers)
    if response.status_code != 200:
        print(f"Error: Could not set {repo_name} to private.")
    else:
        print(f"{repo_name} is now private.")

print("Done!")
