import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# 1. Get all issues in MCP project not in 'In Progress'
jql = "project = MCP AND status != 'In Progress'"
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
    # 3. Find the transition ID for 'In Progress'
    in_progress_id = None
    for t in transitions:
        if t["name"].lower() == "in progress":
            in_progress_id = t["id"]
            break
    if not in_progress_id:
        print(f"No 'In Progress' transition for {issue_key}")
        continue
    # 4. Transition the issue
    transition_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/transitions"
    payload = {"transition": {"id": in_progress_id}}
    result = requests.post(transition_url, json=payload, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
    print(f"Transitioned {issue_key} to 'In Progress':", result.status_code)
