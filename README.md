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
|------|-------------|
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

Run:

```bash
python ./tests/test_document_server.py
```

Expected:

```bash
Available MCP tools:
- list_documents
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