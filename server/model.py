from pydantic import BaseModel


class Item(BaseModel):
    name: str
    quantity: int
    unit: str


class MenuItem(BaseModel):
    name: str
    price: int
    ingredients: list


class ItemCost(BaseModel):
    name: str
