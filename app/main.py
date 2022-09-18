import time
from fastapi import FastAPI, Request

from app.routers import router


description = """
BaseApp as a project for backend course 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (implemented).
* **Read users** (implemented).
"""

app = FastAPI(
    debug=True,
    title="App",
    description=description,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/docs/redoc",
    contact={
        "name": "Shakirov Renat",
        "email": "renatshk@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(router=router)
