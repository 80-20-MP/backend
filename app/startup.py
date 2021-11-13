from concurrent.futures import ProcessPoolExecutor

from .config import settings
from .main import app


@app.on_event("startup")
def init_executor():
    app.state.executor = ProcessPoolExecutor(max_workers=settings.max_workers)


@app.on_event("shutdown")
def close_executor():
    app.state.executor.shutdown(wait=True)
