import uuid
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, NVARCHAR, NTEXT, BIT, DATETIMEOFFSET, INTEGER, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.database import Base


class OutscraperLocation(Base):
    __tablename__ = "rmertDLMOutscraperLocation"

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    MetricId = Column(UNIQUEIDENTIFIER, ForeignKey("rmertDLMOutscraperLocationMetric.Id"), nullable=True)
    PlaceId = Column(NVARCHAR(255), nullable=True)
    GoogleId = Column(NVARCHAR(255), nullable=True)
    Name = Column(NVARCHAR(1000), nullable=True)
    Type = Column(NVARCHAR(255), nullable=True)
    Phone = Column(NVARCHAR(255), nullable=True)
    FullAddress = Column(NVARCHAR(4000), nullable=True)
    PostalCode = Column(NVARCHAR(10), nullable=True)
    State = Column(NVARCHAR(255), nullable=True)
    Latitude = Column(DECIMAL(19,4), nullable=True)
    Longitude = Column(DECIMAL(19,4), nullable=True)
    Verified = Column(BIT, nullable=True)
    LocationLink = Column(NTEXT, nullable=True)
    Country = Column(NVARCHAR(255), nullable=True)
    CountryCode = Column(NVARCHAR(10), nullable=True)
    Timezone = Column(NVARCHAR(255), nullable=True)

    metrics = relationship("OutscraperLocationMetric",
                          primaryjoin="OutscraperLocation.Id == OutscraperLocationMetric.LocationId",
                          back_populates="location")

    latest_metric = relationship("OutscraperLocationMetric",
                               primaryjoin="OutscraperLocation.MetricId == OutscraperLocationMetric.Id",
                               uselist=False,
                               foreign_keys=[MetricId])

    def __repr__(self):
        return f"<OutscraperLocation(Id={self.Id}, Name={self.Name})>"
    

class OutscraperLocationMetric(Base):
    __tablename__ = "rmertDLMOutscraperLocationMetric"

    Id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    LocationId = Column(UNIQUEIDENTIFIER, ForeignKey("rmertDLMOutscraperLocation.Id"), nullable=True)
    Rating = Column(DECIMAL(19,4), nullable = True)
    Reviews = Column(INTEGER, nullable=True)
    ReviewsPerScore1 = Column(INTEGER, nullable=True)
    ReviewsPerScore2 = Column(INTEGER, nullable=True)
    ReviewsPerScore3 = Column(INTEGER, nullable=True)
    ReviewsPerScore4 = Column(INTEGER, nullable=True)
    ReviewsPerScore5 = Column(INTEGER, nullable=True)
    PhotosCount = Column(INTEGER, nullable=True)
    CreateDate = Column(DATETIMEOFFSET(7), nullable=True, default = datetime.now().replace(tzinfo=timezone.utc))
    Year = Column(INTEGER, nullable=True)
    Month = Column(INTEGER, nullable=True)

    location = relationship("OutscraperLocation",
                          primaryjoin="OutscraperLocationMetric.LocationId == OutscraperLocation.Id",
                          back_populates="metrics",
                          foreign_keys=[LocationId])

    referenced_by = relationship("OutscraperLocation",
                               primaryjoin="OutscraperLocationMetric.Id == OutscraperLocation.MetricId",
                               uselist=False,
                               foreign_keys=[OutscraperLocation.MetricId],
                               overlaps="location,metrics,latest_metric")

    def __repr__(self):
        return f"<OutscraperLocationMetric(Id={self.Id}, LocationId={self.LocationId}, Rating={self.Rating})>"















# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     full_name = Column(String, index=True)
#     hashed_password = Column(String)

#     items = relationship("Item", back_populates="owner")

# class Item(Base):
#     __tablename__ = 'items'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey('users.id'))

#     owner = relationship("User", back_populates="items")