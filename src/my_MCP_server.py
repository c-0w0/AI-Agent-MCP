from mcp.server.fastmcp import FastMCP
import weather_tools
import system_tools

# Initialize FastMCP server
mcp = FastMCP("weather and host info mcp", log_level="ERROR")
mcp.add_tool(weather_tools.get_weather_forecast)
mcp.add_tool(system_tools.get_host_info)

def main() -> None:
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()