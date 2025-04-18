from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional

from app.db.database import get_db
from app.schemas.models import Location, LocationMetric, LocationWithMetrics, LocationCounts
from app.services.location.location_service import ( 
    get_location, get_locations, get_location_metrics, get_metrics_by_rating, get_metrics_by_year_month,
    get_location_counts, get_location_with_metrics, get_locations_with_metrics 
    )

router = APIRouter()

# Fixed Path first
@router.get("/locations/metrics/by-rating", response_model=List[LocationMetric])
def read_metrics_by_rating(
    min_rating: float = Query(0, ge=0, le=5),
    max_rating: float = Query(5, ge=0, le=5),
    db: Session = Depends(get_db),
):
    if min_rating > max_rating:
        raise HTTPException(status_code=400, detail="Min Rating cannot be greater than Max Rating")

    metrics = get_metrics_by_rating(db, min_rating=min_rating, max_rating=max_rating)
    return metrics

@router.get("/locations/metrics/by-year-month", response_model=List[LocationMetric])
def read_metrics_by_year_month(
    year: int = Query(..., ge=2000, le=2100, description="Filter by year"),
    month: Optional[int] = Query(None, ge=1, le=12, description="Filter by month"),
    db: Session = Depends(get_db)
):
    if month and (month < 1 or month > 12):
        raise HTTPException(status_code=400, detail="Month must be between 1 and 12")
    
    if year < 2000 or year > 2100:
        raise HTTPException(status_code=400, detail="Year must be between 2000 and 2100")

    metrics = get_metrics_by_year_month(db, year=year, month=month)
    return metrics

@router.get("/locations/counts", response_model=LocationCounts)
def read_location_counts(
    db: Session = Depends(get_db)
):
    return get_location_counts(db)

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

@router.get("/locations/with-metrics", response_model=List[LocationWithMetrics])
def read_locations_with_metrics(
    skip: int = 0, 
    limit: int = 100,
    name: Optional[str] = None,
    country: Optional[str] = None,
    state: Optional[str] = None,
    db: Session = Depends(get_db)
):
    locations = get_locations_with_metrics(db, skip=skip, limit=limit, name=name, country=country, state=state)
    return locations


# Dynamic Path second
@router.get("/locations/{location_id}", response_model=Location)
def read_location(
    location_id: UUID,
    db: Session = Depends(get_db)
):
    location = get_location(db, location_id=location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.get("/locations/{location_id}/metrics", response_model=List[LocationMetric])
def read_location_metrics(location_id: UUID, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrics = get_location_metrics(db, location_id=location_id, skip=skip, limit=limit)
    return metrics

@router.get("/locations/{location_id}/with-metrics", response_model=LocationWithMetrics)
def read_location_with_metrics(location_id: UUID, db: Session = Depends(get_db)):
    location = get_location_with_metrics(db, location_id=location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return location

