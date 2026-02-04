from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get("/")
def first_example():
    return {"data": {'name': "FastAPI"}}


@app.get("/blog/{id}")
def index(id: int):
    return {"index": id}


@app.get("/blog")
def show(limit=8, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f'{limit} published blog from the DB'}
    else:
        return {"data": f'{limit} blog from the DB'}

