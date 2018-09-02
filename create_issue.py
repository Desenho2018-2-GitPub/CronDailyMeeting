import json
import requests
import os
import datetime

with open('env.json') as env_file:
    env_data = json.load(env_file)

with open('secret.json') as secret_file:
    secret_data = json.load(secret_file)

API_TOKEN = secret_data['GITHUB_API_TOKEN']
GITHUB_ORG = env_data['GITHUB_ORGANIZATION']
GITHUB_REPO = env_data['GITHUB_REPOSITORY']
API_URL = "https://api.github.com/repos/" + GITHUB_ORG + "/"+ GITHUB_REPO + "/issues"

DATE = datetime.datetime.now()
DAY = DATE.day
MONTH = DATE.month
YEAR = DATE.year
ISSUE_BODY_TITLE = "# Daily dia ({:02}/{:02}/{:04})\n\n".format(DAY, MONTH, YEAR)

fp = open("issue_body.md", "r", encoding='utf-8')
file_content = fp.read()
fp.close()

ISSUE_TITLE = "Daily {:02}/{:02}".format(DAY, MONTH)
ISSUE_FULL_BODY = ISSUE_BODY_TITLE + file_content

ASSIGNEES_ARRAY = [
    'arthurbdiniz',
    'gabrielziegler3',
    'joao4018',
    'KahCosta',
    'RomeuCarvalhoAntunes',
    'victorcmoura',
    'vitorfhc',
    'wdresende'
]

issue = {
    'title': ISSUE_TITLE,
    'body': ISSUE_FULL_BODY,
    'labels': ['daily'],
    'assignees': ASSIGNEES_ARRAY
    }

response = requests.post(API_URL,
		headers = {'Authorization': 'token ' + API_TOKEN},
		data = json.dumps(issue)
        )

json_content = json.loads(response.content.decode('utf8').replace("'", '"'))

ISSUE_ID = json_content['number']

env_data['LAST_CREATED_ISSUE_ID'] = int(ISSUE_ID)

with open('env.json', 'w') as env_file:
    json.dump(env_data, env_file)

print("Issue #" + str(ISSUE_ID) + "was created")
