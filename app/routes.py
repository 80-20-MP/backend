import asyncio
from concurrent.futures import Executor

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request

from .processing import normalize_tag
from .processing import process_query

router = APIRouter()


def depends_executor(request: Request) -> Executor:
    return request.app.state.executor


@router.get("/query", response_model=list[str])
async def tags_query(query: str, executor: Executor = Depends(depends_executor)):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, process_query, query)


@router.get("/normalize", response_model=list[str])
async def tags_normalize(tag: str, executor: Executor = Depends(depends_executor)):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, normalize_tag, tag)
