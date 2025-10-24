from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import crud
import models
import schemas
from database import engine, SessionLocal

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.get("/items")
def read_items():
    db = SessionLocal()
    items = crud.get_items(db)
    db.close()
    return items

@app.post("/items")
def create_item(item: schemas.ItemCreate):
    db = SessionLocal()
    new_item = crud.create_item(db, item)
    db.close()
    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: schemas.ItemCreate):
    db = SessionLocal()
    updated_item = crud.update_item(db, item_id, item)
    db.close()
    return updated_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = SessionLocal()
    deleted_item = crud.delete_item(db, item_id)
    db.close()
    return deleted_item