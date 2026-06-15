{
  "name": "law-housing-mcp",
  "version": "1.1.0",
  "description": "Housing law MCP with motions and case tools.",
  "tools": [
    { "name": "lookup_lottery", ... },
    { "name": "eligibility_check", ... },
    { "name": "rent_stabilization", ... },
    {
      "name": "draft_motion",
      "description": "Generate a draft housing court motion.",
      "input_schema": {
        "type": "object",
        "properties": {
          "case_type": { "type": "string" },
          "role": { "type": "string" },
          "facts": { "type": "string" },
          "relief_sought": { "type": "string" }
        },
        "required": ["case_type", "role", "facts"]
      }
    },
    {
      "name": "case_summary",
      "description": "Summarize a housing case for reuse.",
      "input_schema": {
        "type": "object",
        "properties": {
          "index_number": { "type": "string" },
          "court": { "type": "string" },
          "parties": { "type": "array", "items": { "type": "string" } },
          "issues": { "type": "array", "items": { "type": "string" } }
        },
        "required": ["index_number", "court"]
      }
    }
  ]
}