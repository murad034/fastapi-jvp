print("Hello World")

# from fastapi import Fastapi
from fastapi import FastAPI
from enum import Enum

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

#query parameter

fake_items_db = [
        { "item_name" : "Foo 1"},
        { "item_name" : "Foo 2"},
        { "item_name" : "Foo 3"},
        { "item_name" : "Foo 4"},
        { "item_name" : "Foo 5"},
        { "item_name" : "Foo 6"},
        { "item_name" : "Foo 7"}
    ]

@app.get("/items")
async def list_items(skip: int=1, limit: int=10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {
        "item_id" : item_id
    }


@app.get("/users")
async def list_users():
    return {
        "message" : "list user routes"
    }


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {
        "user_id" : user_id
    }


@app.get("/users/me")
async def get_current_user():
    return {
        "message" : "this is the current user"
    }

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {
            "food_name" : food_name,
            "message" : "you are healthy"
        }


    if food_name.value == "fruits":
        return {
            "food_name" : food_name,
            "message": "You are still healthy, but like sweet things"
        }
    
    return {
        "food_name" : food_name.value,
        "message": "I like chocolate milk"
    }