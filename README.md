# Azure MCP Knowledge Hub

A Model Context Protocol (MCP) based knowledge platform built with Azure services.

The project demonstrates a multi-server MCP architecture using Azure Storage, Azure SQL, and AI-powered tools.

## Current Status

🚧 Under active development

Implemented:

- ✅ Document MCP Server
- ✅ Azure Blob Storage integration
- ✅ Document listing tool

Planned:

- MCP Client
- Employee MCP Server
- Azure SQL integration
- Azure Bicep deployment
- Monitoring and CI/CD

---

# Architecture

The platform consists of independent MCP services:

             MCP Client
                 |
    +------------+------------+
    |                         |
    v                         v
Document MCP Server Employee MCP Server
    |                         |
    v                         v
Azure Blob Storage     Azure SQL Database

---

# Infrastructure:

- Azure App Service
- Azure Storage Account
- Azure SQL Database
- Azure Key Vault
- Azure Monitor

---

# Tech Stack

- Python
- FastMCP
- Azure Blob Storage
- Azure SQL Database
- Azure Identity
- Azure Bicep

---

# Document MCP Server

The Document MCP Server provides MCP tools for accessing documents stored in Azure Blob Storage.

## Available Tools

| Tool | Description |
|-|-|
| `list_documents` | Returns available documents |
| `search_documents` | Searches documents by name |
| `get_document` | Retrieves document content |

---

# Local Development

## Prerequisites

Install:

- Python 3.11+
- Azure CLI

Login to Azure:

```bash
az login
```

---

# Installation

## Clone repository:

```bash
git clone https://github.com/vaibhav-k/azure-mcp-knowledge-hub.git
cd azure-mcp-knowledge-hub
```

## Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Configuration

Create environment file:

```bash
cp .env.example .env
```

Update:

```bash
AZURE_STORAGE_ACCOUNT_URL=https://<storage-account>.blob.core.windows.net
AZURE_STORAGE_CONTAINER_NAME=documents
```

Example:

```bash
AZURE_STORAGE_ACCOUNT_URL=https://azmcpstorage.blob.core.windows.net
AZURE_STORAGE_CONTAINER_NAME=documents
```

---

# Authentication

The application uses Azure:

```bash
DefaultAzureCredential
```

For local development:

```bash
az login
```

For Azure deployment:

- Managed Identity will be used.

---

# Running the Document MCP Server

From repository root:

```bash
python ./document_server/app.py
```

Expected output:

```bash
Starting MCP server 'Document Server'
```

---

# Testing

## Document MCP Server Test

Run the test:

```bash
python ./tests/test_document_server.py
```

Expected output:

```bash
Available MCP tools:
- list_documents
- search_documents
- get_document
```

---

## Employee MCP Server Test

Run:

```bash
python ./tests/test_employee_server.py
```

Expected output:

```bash
Available Employee tools:
- list_employees
- get_employee
- search_employees
```

## MCP Client Test

Verify that the MCP client can connect to multiple MCP servers:

```bash
python ./tests/test_client.py
```

Expected output:

```bash
Document MCP Server tools:
- list_documents
- search_documents
- get_document

Employee MCP Server tools:
- list_employees
- get_employee
- search_employees
```

---

# Project Structure

```
azure-mcp-knowledge-hub/

├── client/
├── document_server/
│   ├── app.py
│   ├── schemas.py
│   ├── storage.py
│   └── tools.py
├── employee_server/
├── infrastructure/
├── scripts/
├── tests/
├── docs/
└── README.md
```
---

# Employee MCP Server

The Employee MCP Server exposes employee information through MCP tools.

## Available Tools

| Tool | Description |
|-|-|
| `list_employees` | Returns all employees |
| `get_employee` | Returns employee by ID |
| `search_employees` | Searches employee records |

## Current Storage

Development mode uses an in-memory database.

Production deployment will use Azure SQL Database.

---

# MCP Client

The MCP Client provides a unified interface to multiple MCP servers.

Connected servers:

| Server | Purpose |
|-|-|
| Document MCP Server | Azure Blob Storage knowledge |
| Employee MCP Server | Employee information |

Run:

```bash
python ./client/app.py
```

---

# Development Roadmap
- [x] Create Document MCP Server
- [x] Connect Azure Blob Storage
- [x] Add document search
- [x] Add document content retrieval
- [ ] Add Employee MCP Server
- [ ] Add MCP Client
- [ ] Add Azure deployment templates
- [ ] Add GitHub Actions CI/CD

---

# License

MIT License