# LAW‑MCP Architecture

## Overview
LAW‑MCP is a Modular Command Protocol server designed to automate
legal workflows for housing cases, including:
- Motion drafting
- Case summaries
- Deadline tracking
- Housing law analysis (RS status, lotteries, eligibility)

The system follows the MCP standard:
- mcp.json defines tools and schemas
- server.py routes tool requests
- tools/ contains Python logic for each legal function

---

## System Components

### 1. mcp.json
Defines:
- Server name
- Version
- Description
- Tools
- Input schemas

This file tells the MCP client what capabilities the server exposes.

---

### 2. server.py
Handles:
- POST /run requests
- Tool routing
- JSON responses

This is the central controller of the MCP server.

---

### 3. Tools Directory
Each tool is a Python module that performs a specific legal function.

Current tools include:
- draft_motion.py
- case_summary.py
- deadline_tracker.py
- rent_stabilization.py
- eligibility_check.py
- lookup_lottery.py

Each tool:
- Accepts arguments from the client
- Executes logic
- Returns JSON

---

## Data Flow

1. MCP client loads mcp.json
2. Client discovers available tools
3. User triggers a tool
4. Client sends POST /run with tool + arguments
5. server.py receives request
6. server.py routes to correct tool
7. Tool executes logic
8. Tool returns JSON
9. server.py sends JSON back
10. Client displays result to user

---

## Purpose of LAW‑MCP

LAW‑MCP is designed to:
- Automate housing court filings
- Generate motions and affidavits
- Track deadlines
- Summarize cases
- Analyze housing law data
- Assist tenants in enforcing stipulations

This system is modular and can be expanded with additional tools.
