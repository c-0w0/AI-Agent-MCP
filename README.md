## Introduction
This project explores the boundaries and functionalities of Model Context Protocol, and it's my first contact to MCP, nothing fancy here.

## Characters
| Body    | Actor |
| :-------- | :-------: |
| AI Model  | Gemini-2.5-pro    |
| AI Agent | Cline     |
| MCP Server    | `my_MCP_server`, [Fetch](https://mcp.so/server/fetch/modelcontextprotocol)    |

## Configuration file `cline_mcp_settings.json`
```json
{
  "mcpServers": { 
    "my_MCP_server": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/chun/Desktop/Projects/uv_MCP/src/",
        "run",
        "my_MCP_server.py"
      ]
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

## Result
### `get_host_info()` defined in `system_tools.py`, registered in `my_MCP_server.py`
<img width="925" height="705" alt="get_host_info" src="https://github.com/user-attachments/assets/00e867a5-273e-476a-8d6c-e8babb9796c1" />

### `get_weather_forecast()` defined in `weather_tools.py`, registered in `my_MCP_server.py`
<img width="918" height="703" alt="get_weather_forecast" src="https://github.com/user-attachments/assets/9f8a97a6-6381-4083-8b91-b870d70cac5b" />

### Fetch, registered in `my_MCP_server.py`
<img width="915" height="701" alt="Fetch" src="https://github.com/user-attachments/assets/9b051ea0-df99-4dfb-847b-144647b2eafa" />
