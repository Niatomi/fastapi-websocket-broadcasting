from ..broadcasting.broadcast_scheduler import BroadcastScheduler
from ..config import SERVER_METRICS_REFRESH_TIMER
from .utils import get_server_metrics

resources_scheduler = BroadcastScheduler(
    get_server_metrics,
    SERVER_METRICS_REFRESH_TIMER
)
