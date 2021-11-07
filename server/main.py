from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import db
import json
from model import *
from fastapi.encoders import jsonable_encoder
from fastapi.responses import UJSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    print("Hello World")
    return {"msg": "hello world"}


@app.post("/api/add_item")
async def add_item(item: Item):
    try:
        database = db.client.Restaurant.item_list
        name = item.__dict__['name']
        data = database.find_one({"name": name})
        if data == None:
            database.insert_one(item.__dict__)
        else:
            database.update_one(
                {"name": name}, {"$set": {"quantity": data['quantity'] + item.__dict__['quantity']}})
    except:
        print("Couldn't Insert Data")


@app.get("/api/get_item")
async def get_item():
    try:
        database = db.client.Restaurant.item_list
        data_arr = []
        for x in database.find():
            obj = {}
            obj['name'] = x['name']
            obj['quantity'] = x['quantity']
            obj['unit'] = x['unit']
            data_arr.append(obj)
            # data_arr.append(x)
        print(data_arr)
        return data_arr
    except:
        print("Couldn't Get Items")

# whenever this api is invoked add a new item to the Menu list
# either add new item or update the price of already present one


@app.post("/api/add_to_menu")
async def add_to_menu(req: MenuItem):
    try:
        print(req.__dict__)
        database = db.client.Restaurant.Menu
        name = req.__dict__['name']
        data = database.find_one({'name': name})
        if data == None:
            database.insert_one(req.__dict__)
            return {"message": "Item Added to Menu"}
        else:
            database.update_one(
                {'name': name}, {"$set": {"price": req.__dict__['price']}})
            return {"message": "Item Price Updated"}
    except:
        print("Cant add to Menu")


# @app.post("/api/add_order")
# async def add_order():
    # add to order list(new collection) and subract those ingredients from them from the item list


@app.get("/api/get_menu")
async def get_menu():
    try:
        database = db.client.Restaurant.Menu
        data_arr = []
        for x in database.find():
            obj = {}
            obj['name'] = x['name']
            obj['price'] = x['price']
            data_arr.append(obj)
        print(data_arr)
        return data_arr
    except:
        print("Couldn't get Menu")
