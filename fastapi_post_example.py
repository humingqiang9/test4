"""
FastAPI POST Endpoint Example

This script demonstrates a FastAPI application with a POST endpoint
that saves received data to a randomly named JSON file.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import uuid
import os

# Initialize FastAPI app
app = FastAPI(title="POST Endpoint Example", description="A simple FastAPI app with a POST endpoint")

# Define data model
class PostData(BaseModel):
    name: str
    email: str
    message: str

# POST endpoint that saves data to a file
@app.post("/submit", summary="Submit data", description="Accepts POST requests with name, email, and message, then saves to a random file")
async def submit_data(data: PostData):
    # Generate a random filename
    filename = f"{uuid.uuid4().hex}.json"
    
    # Save data to file
    try:
        with open(filename, "w") as f:
            json.dump(data.dict(), f)
        return {"message": "Data saved successfully", "filename": filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving data: {str(e)}")

# Health check endpoint
@app.get("/health", summary="Health check", description="Returns the health status of the application")
async def health_check():
    return {"status": "OK"}

if __name__ == "__main__":
    # Instructions for running the application
    print("To run this FastAPI application, use the following command:")
    print("uvicorn fastapi_post_example:app --host 0.0.0.0 --port 8000 --reload")
    print("\nThen send a POST request to http://localhost:8000/submit with JSON data like:")
    print('{"name": "John Doe", "email": "john@example.com", "message": "Hello World"}')