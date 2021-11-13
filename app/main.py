from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router

__all__ = ("app",)

app = FastAPI(title="Tags 80/20")

from .startup import *  # noqa

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/tags")
