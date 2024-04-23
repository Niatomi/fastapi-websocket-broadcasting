import json
from random import randint


def get_random_metrics() -> str:
    return json.dumps(
        {
            "data_1": randint(1, 5),
            "data_2": randint(1, 5)
        }
    )
