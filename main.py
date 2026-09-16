from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': "hello world!"}


@app.get("/about")
def about():
    return {"about": "Just building around, engineering everywhere"}


@app.post("/registration-form")
def registration():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    return name, age

