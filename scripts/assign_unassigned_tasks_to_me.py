import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# 1. Get all unassigned issues in MCP project
jql = "project = MCP AND assignee IS EMPTY"
search_url = f"{JIRA_URL}/rest/api/3/search"
search_params = {
    "jql": jql,
    "fields": "key"
}
search_response = requests.get(search_url, params=search_params, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
issues = search_response.json().get("issues", [])

for issue in issues:
    issue_key = issue["key"]
    print(f"Assigning {issue_key} to {JIRA_USERNAME}")
    assign_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/assignee"
    payload = {"accountId": None}  # Will fetch accountId below
    # Get accountId for the username
    user_url = f"{JIRA_URL}/rest/api/3/user/search?query={JIRA_USERNAME}"
    user_response = requests.get(user_url, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
    users = user_response.json()
    if users:
        payload["accountId"] = users[0]["accountId"]
        assign_response = requests.put(assign_url, json=payload, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
        print(f"Assigned {issue_key}: {assign_response.status_code}")
    else:
        print(f"Could not find accountId for {JIRA_USERNAME}")
