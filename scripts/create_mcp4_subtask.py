import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

parent_issue_key = "MCP-4"
subtask_summary = "SQL-AI Engine Implementation"
subtask_description = "Implement the SQL-AI engine as described in MCP-4 and the Confluence page: https://techgadgets1230.atlassian.net/wiki/x/AoAE\n\n- Parse natural language queries to SQL\n- Integrate with PostgreSQL, MySQL, etc.\n- Provide REST API for query submission and result retrieval\n- Implement authentication and authorization\n- Robust error handling and logging\n- Document API and provide usage examples\n- Timeline: 4 weeks\n- Acceptance: 80% query coverage, API docs, integration tests\n- Stakeholders: Data Engineering, Backend, QA"

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
        "parent": {
            "key": parent_issue_key
        },
        "summary": subtask_summary,
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": subtask_description
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Subtask"
        }
    }
}

response = requests.post(url, json=payload, headers=headers, auth=auth)
print(response.status_code, response.json())
