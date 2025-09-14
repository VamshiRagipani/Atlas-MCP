import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

issue_url = f"{JIRA_URL}/rest/api/3/issue/createmeta?projectKeys=MCP"
response = requests.get(issue_url, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
meta = response.json()
project_meta = meta.get('projects', [{}])[0]
issue_types = project_meta.get('issuetypes', [])
for itype in issue_types:
    print(f"Issue Type Name: {itype.get('name')}")
