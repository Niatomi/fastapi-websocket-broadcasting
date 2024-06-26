from fastapi import (
    APIRouter,
    WebSocket
)
from .broadcaster import scheduler
import asyncio


router = APIRouter(prefix='/random/metrics')


@router.websocket('/connect/')
async def websocket_endpoint(websocket: WebSocket):
    await scheduler.ws.connect(websocket)
    while True:
        if websocket not in scheduler.ws:
            break
        await asyncio.sleep(5)
