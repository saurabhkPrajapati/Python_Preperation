from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False


@app.post("/blog1")
def create(request: Blog):
    return {"data": f"Blog created with title {request.title}"}


@app.post("/blog2")
def create_blog(title: str, body: str):
    return {'title': title, 'body': body}



# if __name__ == "__main__""":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
