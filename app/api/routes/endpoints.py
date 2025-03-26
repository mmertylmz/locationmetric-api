from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import get_db


router = APIRouter()

# @router.get("/")
# async def read_root():
#     return {"message": "Welcome to the FastAPI application!"}

# @router.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "query": q}

@router.get("/health/database")
def check_database_connection(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        if result.scalar() == 1:
            return {"status": "ok", "message": "Database connection successful"}
        return {"status": "error", "message": "Unknown database error"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")