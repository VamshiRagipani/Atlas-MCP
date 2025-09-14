import os
from jira import JIRA
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

def create_issue(project_key, summary, description):
    jira = JIRA(
        server=JIRA_URL,
        basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN)
    )
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},
    }
    issue = jira.create_issue(fields=issue_dict)
    print(f"Created issue {issue.key}")
    return issue.key

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Create Jira Issue")
    parser.add_argument('--project', required=True)
    parser.add_argument('--summary', required=True)
    parser.add_argument('--description', required=True)
    args = parser.parse_args()
    create_issue(args.project, args.summary, args.description)