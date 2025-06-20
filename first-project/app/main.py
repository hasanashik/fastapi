from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_route():
    return {"message": "Hello, World!"}
# Path parameters
# http://172.30.87.239:8000/items/11
@app.get("/items/{item_id}")
async def read_item(item_id: int)-> dict:
    return {"item_id": item_id}

# Query Parameters
# http://172.30.87.239:8000/filter/?category=books&price_lt=20.5
@app.get("/filter/")
async def filter_items(category: str, price_lt: float):
	return {
		"category": category,
		"price_less_than": price_lt
	}

# Optional Query Parameters
# http://172.30.87.239:8000/search/
# http://172.30.87.239:8000/search/?q=cat&skip=0&limit=5
from typing import Optional
@app.get("/search/")
async def search_items(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    results = {"items": [{"item_id": "123"}, {"item_id": "456"}]}
    if q:
        results.update({"q": q})
    return results
