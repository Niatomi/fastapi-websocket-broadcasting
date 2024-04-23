import json
import psutil


def get_server_metrics() -> str:
    return json.dumps(
        psutil.getloadavg()
    )
