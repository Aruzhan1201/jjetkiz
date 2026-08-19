import uuid

from sqlalchemy import Boolean, Column, Integer, Float, String, Uuid
from .user_model import Base


class DriverProfile(Base):
    __tablename__ = "driver_profiles"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id = Column(Uuid, nullable=False, unique=True)
    vehicle_brand = Column(String(100), nullable=False)
    vehicle_plate_number = Column(String(20), nullable=False, unique=True)
    capacity_kg = Column(Integer, nullable=False)
    capacity_m3 = Column(Integer, nullable=False)
    has_refrigerator = Column(Boolean, default=False, nullable=False)
    vehicle_type = Column(String(20), nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    current_status = Column(String(20), nullable=False, default="offline")
    rating_completed_trips = Column(Integer, default=0, nullable=False)
    rating_failed_trips = Column(Integer, default=0, nullable=False)
