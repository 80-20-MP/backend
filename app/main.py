from fastapi import FastAPI

from .routes import router

__all__ = ("app",)

app = FastAPI(title="Tags 80/20")

from .startup import *  # noqa

app.include_router(router, prefix="/tags")
