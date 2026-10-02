from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    name: str

@app.get("/")
def home():
    return {"message": "VS Code Server POC Running"}

@app.post("/submit")
def submit(data: UserRequest):
    return {
        "input_name": data.name,
        "output": f"Hello {data.name}"
    }
