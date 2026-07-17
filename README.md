# Azure MCP Knowledge Hub

A Model Context Protocol (MCP) based knowledge platform built with Azure services.

This project demonstrates a multi-server MCP architecture where independent MCP servers provide access to enterprise knowledge sources using Azure Storage, Azure SQL Database, and secure Azure services.

---

# Current Status

✅ MVP complete

Implemented:

* ✅ Document MCP Server
* ✅ Employee MCP Server
* ✅ MCP Client supporting multiple MCP servers
* ✅ Azure Blob Storage integration
* ✅ Azure SQL Database integration
* ✅ Azure Key Vault secret management
* ✅ Azure App Service deployment
* ✅ Azure Bicep infrastructure deployment

---

# Architecture

The platform uses a multi-server MCP architecture:

```
                         MCP Client
                              |
              +---------------+---------------+
              |                               |
              v                               v
     Document MCP Server              Employee MCP Server
              |                               |
              v                               v
     Azure Blob Storage              Azure SQL Database


                 Azure Key Vault
                       |
                       |
              Application Secrets
```

## Request Flow

1. MCP Client connects to multiple MCP servers.
2. Document MCP Server provides document knowledge from Azure Blob Storage.
3. Employee MCP Server provides employee information from Azure SQL Database.
4. Secrets are securely managed through Azure Key Vault.
5. Azure App Service Managed Identity is used for Azure authentication.

---

# Azure Infrastructure

The infrastructure is deployed using Azure Bicep.

Provisioned resources:

* Azure App Service Plan
* Document MCP App Service
* Employee MCP App Service
* Azure Storage Account
* Blob Container
* Azure SQL Database (existing SQL Server)
* Azure Key Vault
* Application Insights / Azure Monitor

---

# Tech Stack

## Application

* Python 3.12+
* FastMCP
* SQLAlchemy
* PyODBC
* Rich (terminal UI formatting)

## Azure Services

* Azure Blob Storage
* Azure SQL Database
* Azure Key Vault
* Azure App Service
* Azure Monitor
* Azure Identity
* Azure Bicep

---

# MCP Servers

## Document MCP Server

The Document MCP Server provides MCP tools for accessing documents stored in Azure Blob Storage.

## Available Tools

| Tool               | Description                 |
| ------------------ | --------------------------- |
| `list_documents`   | Returns available documents |
| `search_documents` | Searches documents by name  |
| `get_document`     | Retrieves document content  |

Configuration:

```env
AZURE_STORAGE_ACCOUNT_URL=https://<storage-account>.blob.core.windows.net/
AZURE_STORAGE_CONTAINER_NAME=<container-name>
```

---

## Employee MCP Server

The Employee MCP Server exposes employee information through MCP tools.

## Available Tools

| Tool               | Description                   |
| ------------------ | ----------------------------- |
| `list_employees`   | Returns all employees         |
| `get_employee`     | Returns employee records      |
| `search_employees` | Searches employee information |

Database:

* Azure SQL Database
* SQLAlchemy ORM
* ODBC Driver 18 for SQL Server

Configuration:

```env
DB_SERVER=<sql-server>.database.windows.net
DB_DATABASE=<database-name>
DB_USERNAME=<sql-user>
DB_PASSWORD=<sql-password>
```

In Azure deployment:

* Connection string is stored in Azure Key Vault.
* App Service retrieves it using Key Vault references.

---

# MCP Client

The MCP Client connects to multiple MCP servers and provides a unified MCP interface.

Connected servers:

| Server              | Purpose                      |
| ------------------- | ---------------------------- |
| Document MCP Server | Azure Blob Storage knowledge |
| Employee MCP Server | Employee information         |

Run locally:

```bash
python -m client.app
```

## Example

The MCP Client uses Rich to provide readable terminal output.

Example:

```bash
========== MCP Client ==========

Documents
Employees
Exit

Select server: 2

Employees Tools

| ID | Tool             |
| -- | ---------------- |
| 1  | list_employees   |
| 2  | get_employee     |
| 3  | search_employees |

```

Tool responses are rendered as formatted tables instead of raw JSON.

---

# Local Development

## Prerequisites

Install:

* Python 3.12+
* Azure CLI

Login:

```bash
az login
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/vaibhav-k/azure-mcp-knowledge-hub.git

cd azure-mcp-knowledge-hub
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Configuration

Create environment file:

```bash
cp .env.example .env
```

Example:

```env
AZURE_STORAGE_ACCOUNT_URL=https://<storage-account>.blob.core.windows.net
AZURE_STORAGE_CONTAINER_NAME=documents

DATABASE_URL=<azure-sql-connection-string>
```

---

# Authentication

The application uses:

```python
DefaultAzureCredential
```

## Local Development

Authenticate using Azure CLI:

```bash
az login
```

## Azure Deployment

Azure App Services use:

* System Assigned Managed Identity
* Azure Key Vault references
* Azure Storage authentication

No credentials are stored in application code.

---

# Running Locally

## Document MCP Server

```bash
python -m document_server.app
```

Expected:

```
Starting MCP server 'Document Server'
```

---

## Employee MCP Server

```bash
python -m employee_server.app
```

Expected:

```
Starting Employee MCP Server
```

---

## MCP Client

```bash
python -m client.app
```

The client connects to:

* Document MCP Server
* Employee MCP Server

---

# Testing

## Document MCP Server

```bash
python ./tests/test_document_server.py
```

Expected:

```
Available MCP tools:
- list_documents
- search_documents
- get_document
```

---

## Employee MCP Server

```bash
python ./tests/test_employee_server.py
```

Expected:

```
Available Employee tools:
- list_employees
- get_employee
- search_employees
```

---

## MCP Client

```bash
python ./tests/test_client.py
```

Expected:

```
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

# Azure Deployment

Build Bicep:

```bash
az bicep build \
 --file ./infrastructure/main.bicep
```

Deploy:

```bash
az deployment group create \
 --resource-group <resource-group-name> \
 --template-file ./infrastructure/main.bicep \
 --parameters databaseUrl="<azure-sql-connection-string>"
```

Deployment creates:

* MCP App Services
* Storage resources
* Key Vault
* Monitoring resources

---

# Project Structure

```
azure-mcp-knowledge-hub/

├── client/
│   ├── app.py
│   ├── router.py
│   └── session.py
│
├── document_server/
│   ├── app.py
│   ├── schemas.py
│   ├── storage.py
│   └── tools.py
│
├── employee_server/
│   ├── app.py
│   ├── database.py
│   ├── schemas.py
│   └── tools.py
│
├── infrastructure/
│   ├── main.bicep
│   ├── appservice.bicep
│   ├── storage.bicep
│   ├── sql.bicep
│   ├── keyvault.bicep
│   └── monitor.bicep
│
├── scripts/
├── tests/
├── docs/
└── README.md
```

---

# Development Roadmap

Completed:

* [x] Create Document MCP Server
* [x] Connect Azure Blob Storage
* [x] Add document search
* [x] Add document retrieval
* [x] Create Employee MCP Server
* [x] Add MCP Client
* [x] Deploy Azure infrastructure with Bicep
* [x] Integrate Azure Key Vault secrets

Upcoming:

* [ ] Add GitHub Actions CI/CD
* [ ] Add automated integration tests
* [ ] Add AI-powered document search
* [ ] Add Azure AI Search integration
* [ ] Add authentication and authorization layer

---

# License

MIT License