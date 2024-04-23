from fastapi import (
    APIRouter,
    WebSocket
)
from .broadcaster import resources_scheduler
import asyncio


router = APIRouter(prefix='/server/resources')


@router.websocket('/connect/')
async def websocket_endpoint(websocket: WebSocket):
    await resources_scheduler.ws.connect(websocket)
    while True:
        if websocket not in resources_scheduler.ws:
            break
        await asyncio.sleep(5)
