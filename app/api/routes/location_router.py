from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional

from app.db.database import get_db
from app.schemas.models import Location, LocationMetric, LocationWithMetrics
from app.services.location_service import ( 
    get_location, get_locations, get_location_with_metrics, get_location_metrics, get_metrics_by_rating 
    )

router = APIRouter()

@router.get("/locations/", response_model=List[Location])
def read_locations(
    skip: int = 0, 
    limit: int = 100,
    name: Optional[str] = None,
    country: Optional[str] = None,
    state: Optional[str] = None,
    db: Session = Depends(get_db)
):
    locations = get_locations(db, skip=skip, limit=limit, name=name, country=country, state=state)
    return locations

