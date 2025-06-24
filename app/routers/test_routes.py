from typing import Annotated, Union

from fastapi import APIRouter, Cookie, HTTPException
from pydantic import BaseModel

from app.models.test import Test

router = APIRouter()


@router.get("/test_param/{param}")
async def test_param(param: str):
    if param == "test":
        raise HTTPException(status_code=400, detail="parameter can not be '"'test'"'")
    return {"param": param}

@router.get("/test_query_param")
async def test_query_param(param: str):
    return {"query_param": param}

@router.get("/test_opt_query_param")
async def test_opt_query_param(param: str | None = None):
    return {"query_param": param}

@router.post("/test_body", response_model=Test)
async def test_body(test: Test) -> Test:
    return test

class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    selected_id: Union[int, None] = None


