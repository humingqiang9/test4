from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uuid

app = FastAPI()

# Model for the POST request data
class PostData(BaseModel):
    name: str
    value: int
    metadata: Dict[str, Any] = None

# In-memory storage for demonstration
storage = {}

@app.post("/data/")
async def create_data_item(data: PostData):
    """
    Accepts a POST request with JSON data and stores it with a unique ID.
    
    Args:
        data (PostData): The data to store
        
    Returns:
        dict: A confirmation message with the stored data and its ID
    """
    # Generate a unique ID for the data item
    item_id = str(uuid.uuid4())
    
    # Store the data
    storage[item_id] = data.dict()
    
    return {
        "message": "Data item created successfully",
        "id": item_id,
        "data": storage[item_id]
    }

@app.get("/data/{item_id}")
async def get_data_item(item_id: str):
    """
    Retrieves a stored data item by its ID.
    
    Args:
        item_id (str): The unique ID of the data item
        
    Returns:
        dict: The stored data item
        
    Raises:
        HTTPException: If the item ID is not found
    """
    if item_id not in storage:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"id": item_id, "data": storage[item_id]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)