# Atlas MCP

Atlas MCP is a Model Context Protocol (MCP) server for Atlassian products, supporting both Confluence and Jira (Cloud and Server/Data Center deployments).

## Features

- **Automatic Jira Updates:** Sync Jira issues from meeting notes
- **AI-Powered Confluence Search:** Find and summarize Confluence content
- **Smart Jira Issue Filtering:** Query urgent bugs or issues by project/date
- **Content Creation & Management:** Create and update Confluence pages and Jira issues

## Compatibility

| Product        | Deployment Type    | Support Status              |
|----------------|--------------------|-----------------------------|
| **Confluence** | Cloud              | ✅ Fully supported           |
| **Confluence** | Server/Data Center | ✅ Supported (version 6.0+)  |
| **Jira**       | Cloud              | ✅ Fully supported           |
| **Jira**       | Server/Data Center | ✅ Supported (version 8.14+) |

## Quick Start

### Authentication Setup

Atlas MCP supports three authentication methods:

- **API Token (Cloud):** Create an API token from your Atlassian account and use it for authentication.
- **Personal Access Token (Server/Data Center):** Generate a PAT from your profile and use it for authentication.
- **OAuth 2.0 (Cloud):** Advanced users can set up OAuth 2.0 for enhanced security.

### Configuration

Configure Atlas MCP using environment variables or an environment file. Common variables include:

- `CONFLUENCE_URL`
- `CONFLUENCE_USERNAME`
- `CONFLUENCE_API_TOKEN`
- `JIRA_URL`
- `JIRA_USERNAME`
- `JIRA_API_TOKEN`
- `ENABLED_TOOLS` (comma-separated list of enabled tools)
- `READ_ONLY_MODE` (set to "true" to disable write operations)

See the `.env.example` file for all available options.

## IDE Integration

Atlas MCP is designed for integration with AI assistants and IDEs. Configure your IDE to connect to the MCP server using the appropriate authentication and environment variables.

## Tools

### Jira Tools

- `jira_get_issue`: Get details of a specific issue
- `jira_search`: Search issues using JQL
- `jira_create_issue`: Create a new issue
- `jira_update_issue`: Update an existing issue
- `jira_transition_issue`: Transition an issue to a new status
- `jira_add_comment`: Add a comment to an issue

### Confluence Tools

- `confluence_search`: Search Confluence content using CQL
- `confluence_get_page`: Get content of a specific page
- `confluence_create_page`: Create a new page
- `confluence_update_page`: Update an existing page

## Troubleshooting

- **Authentication Failures:** Check your API tokens or PATs.
- **SSL Certificate Issues:** For self-signed certificates, set SSL verify variables to "false".
- **Permission Errors:** Ensure your Atlassian account has sufficient permissions.

## Security

- Never share API tokens or PATs.
- Keep `.env` files secure and private.




