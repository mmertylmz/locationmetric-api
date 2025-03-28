from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import get_db
from app.api.routes.locations.location_router import router as location_router


router = APIRouter()

router.include_router(location_router, prefix="/api/v1", tags=["locations"])

@router.get("/health/database")
def check_database_connection(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))
        if result.scalar() == 1:
            return {"status": "ok", "message": "Database connection successful"}
        return {"status": "error", "message": "Unknown database error"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    

