azure-mcp-law-serverfrom mcp.server import Server
from mcp.types import Tool, ToolRequest, ToolResponse

server = Server("law-mcp")

@server.tool(
    Tool(
        name="case_search",
        description="Search for case law",
        input_schema={
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    )
)
def case_search(req: ToolRequest):
    query = req.params["query"]
    return ToolResponse(
        content=f"Results for: {query}"
    )

if __name__ == "__main__":
    server.run()