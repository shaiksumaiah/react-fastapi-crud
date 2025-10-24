import models
import schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session

# 🔍 READ: Get all items from the database
def get_items(db: Session):
    return db.query(models.Item).all()

# 🆕 CREATE: Add a new item to the database
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())  # Convert Pydantic model to SQLAlchemy model
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # Refresh to get the new ID
    return db_item

# ✏️ UPDATE: Modify an existing item by ID
def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

# ❌ DELETE: Remove an item by ID
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}