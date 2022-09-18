from fastapi import APIRouter
from typing import Optional

router = APIRouter()


@router.get("/")
async def root():
    """base function for print hello world

    Returns:
        _type_: _description_
    """

    return {"message": "Hello World"}


@router.get("/items/{item_id}")
async def root(item_id: int):
    """base function for print hello world with item_id

    Returns:
        _type_: _description_
    """

    return {"item_id": item_id}


@router.get("/users/")
async def root(user_id: int, query: Optional[str] = None):
    """base query function

    Returns:
        _type_: _description_
    """
    if query:
        return {"user_id": user_id, "query": query}
    return {"user_id": user_id}
