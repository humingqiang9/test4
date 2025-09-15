from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import uuid
import os

app = FastAPI()

class PostData(BaseModel):
    name: str
    email: str
    message: str

@app.post("/submit")
async def submit_data(data: PostData):
    # Generate a random filename
    filename = f"{uuid.uuid4().hex}.py"
    
    # Create the content for the file
    file_content = f"""# Saved POST data
name = {repr(data.name)}
email = {repr(data.email)}
message = {repr(data.message)}
"""
    
    # Write to the file
    with open(filename, "w") as f:
        f.write(file_content)
    
    return {"filename": filename, "status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)