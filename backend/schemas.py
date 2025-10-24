from pydantic import BaseModel

# Input format
class ItemCreate(BaseModel):
    name: str
    description: str

# Output format (includes ID)
class Item(ItemCreate):
    id: int