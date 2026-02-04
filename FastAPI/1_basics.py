from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def first_example():
    # return {"GFG Example": "FastAPI"}
    return {"data": {'name': "FastAPI"}}


@app.get("/about")
def about():
    return {"data": "About"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}



# since read line by line fastAPI WILL  give error for below lines"
# @app.get("/blog/unpublished")
# def unpublished():
#     return {"data": "This is unpublished"}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {'1', '2'}}


