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
