import uvicorn
from fastapi import FastAPI
from routers import test_routes

app = FastAPI()
app.include_router(test_routes.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload=True)