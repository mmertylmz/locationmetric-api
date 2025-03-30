from pydantic import BaseModel, UUID4
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class LocationMetricBase(BaseModel):
    Rating: Optional[Decimal] = None
    Reviews: Optional[int] = None
    ReviewsPerScore1: Optional[int] = None
    ReviewsPerScore2: Optional[int] = None
    ReviewsPerScore3: Optional[int] = None
    ReviewsPerScore4: Optional[int] = None
    ReviewsPerScore5: Optional[int] = None
    PhotosCount: Optional[int] = None
    Year: Optional[int] = None
    Month: Optional[int] = None

class LocationMetric(LocationMetricBase):
    Id: UUID4
    LocationId: Optional[UUID4] = None
    CreateDate: Optional[datetime] = None

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    PlaceId: Optional[str] = None
    GoogleId: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[str] = None
    Phone: Optional[str] = None
    FullAddress: Optional[str] = None
    State: Optional[str] = None
    Country: Optional[str] = None
    CountryCode: Optional[str] = None

class Location(LocationBase):
    Id: UUID4
    MetricId: Optional[UUID4] = None
    Latitude: Optional[Decimal] = None
    Longitude: Optional[Decimal] = None
    Verified: Optional[bool] = None
    PostalCode: Optional[str] = None
    LocationLink: Optional[str] = None
    Timezone: Optional[str] = None
    
    class Config:
        orm_mode = True

class LocationWithMetrics(Location):
    latest_metric: Optional[LocationMetric] = None
    metrics: List[LocationMetric] = []


class LocationCounts(BaseModel):
    total: int
    verified_count: int
    unverified_count: int
















# class ItemBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int

# class ItemInDB(Item):
#     hashed_password: str

# class UserBase(BaseModel):
#     username: str
#     email: str

# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int
#     is_active: bool

# class UserInDB(User):
#     hashed_password: str

# class Message(BaseModel):
#     message: str

# class ErrorResponse(BaseModel):
#     detail: str

# class SuccessResponse(BaseModel):
#     success: bool
#     data: Optional[dict] = None
#     message: Optional[str] = None