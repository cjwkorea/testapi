from fastapi import FastAPI
from pydantic import BaseModel

class Cat(BaseModel):
    name: str
    id: int = 0

app = FastAPI()


@app.get("/first/{id}")
async def root(id: int):
    return {"message": "Hello World", "id": id}


@app.get("/second")
async def second(skip: int = 0, limit: int = 10):
    # (skip: int = 0, limit: int = 10) 값을 보내지않아도 나오는 기본값
    return {"skip" : skip,  "limit" : limit}


@app.post("/cat")
async def cat(cat: Cat):
    return cat