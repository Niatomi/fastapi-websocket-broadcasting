from fastapi import (
    APIRouter,
    WebSocket
)


router = APIRouter(prefix='/server/resources')


@router.websocket('/connect/')
async def websocket_endpoint(websocket: WebSocket):
    pass
