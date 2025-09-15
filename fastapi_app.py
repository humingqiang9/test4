from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

@app.post("/items/")
async def create_item(item: Item):
    # Generate a random filename
    filename = f"{uuid.uuid4().hex}.py"
    
    # Save the item data to the file
    with open(filename, "w") as f:
        f.write(f"# Item: {item.name}\n")
        f.write(f"description = '{item.description}'\n")
        f.write(f"price = {item.price}\n")
        f.write(f"tax = {item.tax}\n")
        f.write(f"total = {item.price + item.tax}\n")
    
    return {"filename": filename, "item": item}