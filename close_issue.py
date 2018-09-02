import json
import requests
import os

with open('env.json') as env_file:
    env_data = json.load(env_file)

with open('secret.json') as secret_file:
    secret_data = json.load(secret_file)

API_TOKEN = secret_data['GITHUB_API_TOKEN']
GITHUB_ORG = env_data['GITHUB_ORGANIZATION']
GITHUB_REPO = env_data['GITHUB_REPOSITORY']
LAST_CREATED_ISSUE_ID = env_data['LAST_CREATED_ISSUE_ID']
API_URL = "https://api.github.com/repos/" + GITHUB_ORG + "/"+ GITHUB_REPO + "/issues/" + "{0}".format(LAST_CREATED_ISSUE_ID)

content = {
  "state": "closed"
}

response = requests.patch(
  API_URL,
	headers = {'Authorization': 'token ' + API_TOKEN},
	data = json.dumps(content)
)

print("Issue #{0} was closed".format(LAST_CREATED_ISSUE_ID))
