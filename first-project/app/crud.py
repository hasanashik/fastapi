from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage for items
items_db: List[Item] = [
    Item(id=1, name="Item One", description="This is the first item."),
    Item(id=2, name="Item Two", description="This is the second item."),
    Item(id=3, name="Item Three", description="This is the third item."),
]

# GET method to retrieve all items
@app.get("/items/", response_model=List[Item])
async def read_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# POST method to create a new item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items_db.append(item)
    return item

# PUT method to update an existing item by ID
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE method to remove an item by ID
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")