# MCP Server for NYC Housing Law - Case Management

This MCP server provides comprehensive tools for managing housing law cases, particularly for tenant rights, wrongful eviction, property loss, and legal motion generation.

## Features

### Case Management Tools
- **case_lookup** - Search cases by ID, client name, or property address
- **get_full_case_details** - Retrieve complete case data for attorney review
- **get_legal_issues** - Identify all legal issues and grounds for relief
- **get_action_plan** - Step-by-step action plan with document requirements

### Legal Document Generation
- **motion_generator** - Generate motion templates:
  - Motion to Vacate (Inquest default)
  - Motion to Vacate (Eviction/Stay Violation)
  - Motion for Relief from Stay Violation
  - Poor Person Status Affidavit
- **generate_affidavit** - Create sworn statements:
  - Hospitalization-based affidavit
  - Property loss affidavit
  - Stipulation violation affidavit

### Deadline & Document Management
- **deadline_tracker** - Track urgent deadlines and action items
- **track_court_dates** - Upcoming and past court dates with prep notes
- **get_document_checklist** - Complete document tracking with status

### Housing Law Tools (Original)
- **lookup_lottery** - Search NYC Housing Connect lotteries
- **eligibility_check** - Check AMI eligibility
- **rent_stabilization** - Analyze rent stabilization status

## Quick Start

### Installation
```bash
pip install flask
```

### Running the Server
```bash
python server.py
```

Server runs on `http://localhost:8000`

### Health Check
```bash
curl http://localhost:8000/health
```

## Using the Tools

### Example: Case Lookup
```json
{
  "tool": "case_lookup",
  "arguments": {
    "case_id": "PATERSON_RG_001"
  }
}
```

### Example: Generate Motion to Vacate
```json
{
  "tool": "motion_generator",
  "arguments": {
    "case_id": "PATERSON_RG_001",
    "motion_type": "vacate_inquest",
    "include_evidence": true
  }
}
```

### Example: Get Action Plan
```json
{
  "tool": "get_action_plan",
  "arguments": {
    "case_id": "PATERSON_RG_001"
  }
}
```

### Example: Track Deadlines
```json
{
  "tool": "deadline_tracker",
  "arguments": {
    "case_id": "PATERSON_RG_001",
    "action": "urgent"
  }
}
```

### Example: Get Document Checklist
```json
{
  "tool": "get_document_checklist",
  "arguments": {
    "case_id": "PATERSON_RG_001"
  }
}
```

## Case Data Structure

Cases are stored in JSON format in the `cases/` directory with complete information:
- Client and property details
- Housing court case status and stipulations
- Violation documentation
- Legal issues and grounds for relief
- Action plan with 9 steps
- Key documents checklist

## Legal Resources

### Pro Bono/Legal Aid (NYC)
- **Legal Aid Society**: legalaidnyc.org
- **Legal Services NYC**: legalservicesnyc.org
- **NYLAG**: nylag.org
- **Mobilization for Justice**: mfjlegal.org
- **City Bar Justice Center**: citybarjusticecenter.org

### Important Statutes
- **CPLR 5015** - Motion to Vacate Judgment by Default
- **CPLR 1101** - Poor Person Status
- **NY Housing Stability and Tenant Protection Act of 2019**
- **Americans with Disabilities Act (ADA)** - Court accommodations

## Contributing Cases

To add a new case to the system:
1. Create a JSON file in `cases/` directory
2. Follow the structure of `ronald_paterson_case.json`
3. Update server.py if adding new tool types
4. Test with MCP client

## Support

For questions about NYC housing law:
- Contact Legal Aid Society for pro bono representation
- NYC Housing Court: Housing.Court@nycourts.gov
- NY State Courts: e-courts.nycourts.gov
