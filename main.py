print("Hello World")

# from fastapi import Fastapi
from fastapi import FastAPI;

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello from bangladesh"}

@app.get("/", description="This is our first route", deprecated=True)
async def base_get_route():
    return {
            "message": "hello from base get route"
        }

@app.post("/")
async def post():
    return {
        "message" : "hellow world from the post route"
    }

@app.put("/")
async def put():
    return {
        "message" : "hello world from put route"
    }