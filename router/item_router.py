from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schema.item_schema import ItemValidationSchema
from models.item_table import ItemDB
from db.connection import get_db
from typing import List

router = APIRouter();

@router.post("/items", response_model=ItemValidationSchema)
def createDetails(item:ItemValidationSchema, db: Session = Depends(get_db)):
    print("gyufgsdghv", item)
    db_item = ItemDB(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item