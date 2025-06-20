from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_route():
    return {"message": "Hello, World!"}