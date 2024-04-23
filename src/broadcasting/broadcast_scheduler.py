from .connection_manager import ConnectionManager
from typing import Callable
from contextlib import suppress
import asyncio


class BroadcastScheduler:

    def __init__(self,
                 content_func: Callable,
                 timer: int) -> None:
        self.ws_manager: ConnectionManager = ConnectionManager()
        self.content_func: Callable = content_func
        self.timer = timer

        self._task: asyncio.Task = None

    async def _pre_task_start(self):
        ...

    async def _pre_task_cancel(self):
        await self.ws_manager.disconnect_all()

    async def start(self):

        self._task = asyncio.ensure_future(self._run())

    async def stop(self):
        await self._pre_task_cancel()
        self._task.cancel()
        with suppress(asyncio.CancelledError):
            await self._task

    async def _run(self):
        while True:
            need_to_broadcast = await self.ws.is_anybody_on_network()
            print(f"Run with {self.timer}")
            if need_to_broadcast:
                try:
                    await self.ws_manager.broadcast(
                        self.content_func()
                    )
                except Exception:
                    pass
            await asyncio.sleep(self.timer)

    @property
    def ws(self):
        return self.ws_manager
