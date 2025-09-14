import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

url = f"{JIRA_URL}/rest/api/3/project/search"
response = requests.get(url, auth=(JIRA_USERNAME, JIRA_API_TOKEN))
projects = response.json().get("values", [])
for project in projects:
    print(f"Name: {project.get('name')}, Key: {project.get('key')}")
