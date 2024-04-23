from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except ValueError:
            pass

    async def disconnect_all(self):
        buffered_connection = self.active_connections
        for connection in buffered_connection:
            await self.disconnect(connection)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception:
                await self.disconnect(connection)

    async def is_anybody_on_network(self):
        if len(self.active_connections) == 0:
            return False
        return True

    def __contains__(self, item):
        return item in self.active_connections
