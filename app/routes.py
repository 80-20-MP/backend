import asyncio
from concurrent.futures import Executor

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from pydantic import BaseModel

from .processing import normalize_tag
from .processing import process_query

router = APIRouter()


def depends_executor(request: Request) -> Executor:
    return request.app.state.executor


class TagsQueryRequest(BaseModel):
    query: str


@router.post("/query", response_model=list[str])
async def tags_query(
    request: TagsQueryRequest, executor: Executor = Depends(depends_executor)
):
    # TODO: run in subprocess
    return process_query(request.query)


class TagsNormalizeRequest(BaseModel):
    tag: str


@router.post("/normalize", response_model=list[str])
async def tags_normalize(
    request: TagsNormalizeRequest, executor: Executor = Depends(depends_executor)
):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, normalize_tag, request.tag)
