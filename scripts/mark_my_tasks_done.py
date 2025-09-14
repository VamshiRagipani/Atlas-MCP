import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# 1. Get all issues assigned to me in MCP project
jql = f"project = MCP AND assignee = '{JIRA_USERNAME}' AND status != 'Done'"
search_url = f"{JIRA_URL}/rest/api/3/search"
search_params = {
    "jql": jql,
    "fields": "key,status"
}
search_response = requests.get(search_url, params=search_params, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
issues = search_response.json().get("issues", [])

for issue in issues:
    issue_key = issue["key"]
    print(f"Processing {issue_key}")
    # 2. Get available transitions for the issue
    transitions_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/transitions"
    transitions_response = requests.get(transitions_url, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
    transitions = transitions_response.json().get("transitions", [])
    # 3. Find the transition ID for 'Done'
    done_id = None
    for t in transitions:
        if t["name"].lower() == "done":
            done_id = t["id"]
            break
    if not done_id:
        print(f"No 'Done' transition for {issue_key}")
        continue
    # 4. Transition the issue
    transition_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/transitions"
    payload = {"transition": {"id": done_id}}
    result = requests.post(transition_url, json=payload, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
    print(f"Marked {issue_key} as 'Done':", result.status_code)
