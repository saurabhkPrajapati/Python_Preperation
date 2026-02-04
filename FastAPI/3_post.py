from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False


@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog created with title {request.title}"}


@app.get("/blog")
def show(limit: int = 8, published: bool = True, sort: Optional[bool] = None):
    if published:
        return {"data": f'{limit} published blog from the DB'}
    else:
        return {"data": f'{limit} blog from the DB'}


if __name__ == "__main__""":
    uvicorn.run(app, host="127.0.0.1", port=9000)
