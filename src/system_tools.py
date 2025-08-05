from typing import Any
import platform
import psutil
import json

def get_host_info() -> str:
    """get host information

    Returns:
        str: JSON string containing system, CPU, and memory
    """
    info: dict[str, Any] = {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu": {
            "cores_physical": psutil.cpu_count(logical=False),
            "cores_logical": psutil.cpu_count(),
            "model": platform.processor(), # assuming Windows
            "usage_percent": psutil.cpu_percent(interval=1)
        },
        "memory_gb": str(round(psutil.virtual_memory().total / (1024**3), 2))
    }

    return json.dumps(info, indent=4)

# if __name__ == '__main__': # for debugging purpose
#     print(get_host_info())