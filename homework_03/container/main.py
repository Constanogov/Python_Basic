import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def pong():
    return {
        "message": "pong",
    }

@app.get("/")
def hello():
    return {
        "message": "Thank you Mario! But your princess is in another castle",
    }

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )