from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .server_resources.router import router as resoures_router


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


@app.on_event('startup')
async def startup():
    ...


@app.on_event('shutdown')
async def shutdown():
    ...
