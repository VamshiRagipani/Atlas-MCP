import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

url = f"{JIRA_URL}/rest/api/3/issue"
auth = (JIRA_USERNAME, JIRA_API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload = {
    "fields": {
        "project": {
            "key": "MCP"
        },
        "summary": "New Test Task",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Created by MCP "
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Task"
        }
    }
}

response = requests.post(url, json=payload, headers=headers, auth=auth)
print(response.status_code, response.json())

# Create a subtask under the parent issue MCP-2
parent_issue_key = "MCP-2"  # Change this to your parent issue key if needed
subtask_payload = {
    "fields": {
        "project": {
            "key": "MCP"
        },
        "parent": {
            "key": parent_issue_key
        },
        "summary": "Recent Task",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Hi there"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Sub-task"
        }
    }
}

subtask_response = requests.post(url, json=subtask_payload, headers=headers, auth=auth)
print(subtask_response.status_code, subtask_response.json())
