from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import json
import os

app = FastAPI()

class PostData(BaseModel):
    name: str
    email: str
    message: str

@app.post("/submit")
async def submit_data(data: PostData):
    # Generate a random filename
    filename = f"post_data_{uuid.uuid4().hex}.json"
    
    # Save the data to the file
    try:
        with open(filename, "w") as f:
            json.dump(data.dict(), f)
        return {"filename": filename, "message": "Data saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving data: {str(e)}")

@app.get("/")
async def root():
    return {"message": "FastAPI POST endpoint ready"}