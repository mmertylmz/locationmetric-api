from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import get_db
from pydantic import UUID4
from app.db.models import OutscraperLocation
from app.schemas.models import Location


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
    

@router.get("/locations/{location_id}", response_model=Location)
def get_location(location_id: UUID4, db: Session = Depends(get_db)):
    db_location = db.query(OutscraperLocation).filter(OutscraperLocation.Id == location_id).first()
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return db_location