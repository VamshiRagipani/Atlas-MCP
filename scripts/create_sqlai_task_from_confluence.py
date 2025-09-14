import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# Replace with actual requirements and details extracted from the Confluence page
requirements = "Requirements and details extracted from the Confluence page: \n\n- Build a SQL-AI engine that can parse natural language queries and convert them to SQL.\n- Integrate with existing database systems (PostgreSQL, MySQL, etc.).\n- Provide a REST API for query submission and result retrieval.\n- Implement user authentication and authorization.\n- Ensure robust error handling and logging.\n- Document the API and provide usage examples.\n- Timeline: 4 weeks.\n- Stakeholders: Data Engineering, Backend, QA.\n- Acceptance Criteria: \n  * The engine can handle at least 80% of typical business queries.\n  * API documentation is published and reviewed.\n  * Integration tests pass for supported databases.\n\nReference: https://techgadgets1230.atlassian.net/wiki/x/AoAE"

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
        "summary": "Task based on Confluence requirements",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": requirements
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
