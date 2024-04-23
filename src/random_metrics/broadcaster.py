from ..broadcasting.broadcast_scheduler import BroadcastScheduler
from ..config import RANDOM_METRICS_REFRESH_TIMER
from .utils import get_random_metrics

scheduler = BroadcastScheduler(
    get_random_metrics,
    RANDOM_METRICS_REFRESH_TIMER
)
