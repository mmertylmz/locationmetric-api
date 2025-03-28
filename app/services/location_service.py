from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional
from app.db.models import OutscraperLocation, OutscraperLocationMetric

def get_location(db: Session, location_id: UUID) -> Optional[OutscraperLocation]:
    return db.query(OutscraperLocation).filter(OutscraperLocation.Id == location_id).first()

def get_locations(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        name: Optional[str] = None,
        country: Optional[str] = None,
        state: Optional[str] = None,
        type: Optional[str] = None,
) -> List[OutscraperLocation]:
    query = db.query(OutscraperLocation)

    if name:
        query = query.filter(OutscraperLocation.Name.like(f"%{name}%"))

    if country:
        query = query.filter(OutscraperLocation.Country == country)
    
    if state:
        query = query.filter(OutscraperLocation.State == state)

    if type:
        query = query.filter(OutscraperLocation.Type == type)

    query = query.order_by(OutscraperLocation.Name)

    return query.offset(skip).limit(limit).all()


def get_location_with_metrics(db: Session, location_id: UUID) -> Optional[OutscraperLocation]:
    return db.query(OutscraperLocation)\
        .filter(OutscraperLocationMetric.LocationId == location_id)\
        .first()


def get_location_metrics(db:Session, location_id: UUID, skip: int = 0, limit: int = 100) -> List[OutscraperLocationMetric]:
    return db.query(OutscraperLocationMetric)\
        .filter(OutscraperLocationMetric.LocationId == location_id)\
        .order_by(OutscraperLocationMetric.CreateDate.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

def get_metrics_by_rating(db: Session, min_rating: float = 0, max_rating: float = 5, skip: int = 0, limit: int = 100) -> List[OutscraperLocationMetric]:
    """
    get metrics by rating range
    """

    return db.query(OutscraperLocationMetric)\
        .filter(OutscraperLocationMetric.Rating >= min_rating)\
        .filter(OutscraperLocationMetric.Rating <= max_rating)\
        .order_by(OutscraperLocationMetric.CreateDate.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

def get_metrics_by_year_month(db: Session, year: int, month: Optional[int] = None, skip: int = 0, limit: int = 100) -> List[OutscraperLocationMetric]:
    """
    get metrics by year and month
    """

    query = db.query(OutscraperLocationMetric)\
        .filter(OutscraperLocationMetric.CreateDate.year == year)

    if month:
        query = query.filter(OutscraperLocationMetric.CreateDate.month == month)

    return query.order_by(OutscraperLocationMetric.CreateDate.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()
