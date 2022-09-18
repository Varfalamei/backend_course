from fastapi import FastAPI, Request

from app.routers import router

app = FastAPI(
    debug=True,
    title="App",
    description=("BaseApp"),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router=router)
