import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .server_resources_metrics.router import router as resoures_router
from .server_resources_metrics.broadcaster import resources_scheduler

from .random_metrics.router import router as random_metrics_router
from .random_metrics.broadcaster import scheduler as rand_schduler

app = FastAPI(
    title='BroadcastAPI App',
    contact={
        "name": "Danila Sklyarov",
        "url": "https://t.me/niatomi",
        "email": "playervoker@gmail.com",
    },
    summary="BroadcastAPI",
    description="""
    # Description

    """,
    docs_url='/broadcast/docs',
    openapi_url='/broadcast/openapi.json',
    version='0.0.1',
)

app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE", 'PUT', 'PATCH', 'OPTIONS'],
    allow_headers=["*"],
    expose_headers=[
        "Content-Disposition",
        "Content-Type",
        "Content-Length"
    ]
)


app.include_router(resoures_router, prefix='/broadcast')
app.include_router(random_metrics_router, prefix='/broadcast')


@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    loop.create_task(resources_scheduler.start())
    loop.create_task(rand_schduler.start())


@app.on_event('shutdown')
async def shutdown():
    await resources_scheduler.stop()
    await rand_schduler.stop()
    tasks = asyncio.all_tasks()
    for task in tasks:
        task.cancel()
