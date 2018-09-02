import json
import requests
import os
import datetime

API_TOKEN = os.environ['GITHUB_API_TOKEN']
GITHUB_ORG = os.environ['GITHUB_ORGANIZATION']
GITHUB_REPO = os.environ['GIHUB_REPOSITORY']
API_URL = "https://api.github.com/repos/" + GITHUB_ORG + "/"+ GITHUB_REPO + "/issues"

DATE = datetime.datetime.now()
DAY = DATE.day
MONTH = DATE.month
YEAR = DATE.year
ISSUE_BODY_TITLE = "# Daily dia ({:02}/{:02}/{:04})\n\n".format(DAY, MONTH, YEAR)

fp = open("issue_body.md", "r")
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

os.environ["LAST_CREATED_ISSUE_ID"] = "{0}".format(ISSUE_ID)

print(ISSUE_ID)
