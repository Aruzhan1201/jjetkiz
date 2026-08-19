from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class DriverProfileSchema(BaseModel):
    id: UUID
    user_id: UUID
    vehicle_brand: str = Field(..., min_length=1, max_length=100)
    vehicle_plate_number: str = Field(..., min_length=1, max_length=20)
    capacity_kg: float = Field(..., gt=0)
    capacity_m3: float = Field(..., gt=0)
    has_refrigerator: bool
    vehicle_type: str = Field(..., min_length=1)
    is_verified: bool
    current_status: str = Field(..., min_length=1)
    rating_completed_trips: int = Field(default=0, ge=0)
    rating_failed_trips: int = Field(default=0, ge=0)

    class Config:
        from_attributes = True

class DriverProfileCreate(BaseModel):
    user_id: UUID
    vehicle_brand: str = Field(..., min_length=1, max_length=100)
    vehicle_plate_number: str = Field(..., min_length=1, max_length=20)
    capacity_kg: float = Field(..., gt=0)
    capacity_m3: float = Field(..., gt=0)
    has_refrigerator: bool = False
    vehicle_type: str = Field(..., min_length=1)
    is_verified: bool = False
    current_status: str = Field(min_length=1, default="offline")
    rating_completed_trips: int = Field(default=0, ge=0)
    rating_failed_trips: int = Field(default=0, ge=0)

class DriverProfileUpdate(BaseModel):
    vehicle_brand: Optional[str] = Field(None, min_length=1, max_length=100)
    capacity_kg: Optional[float] = Field(None, gt=0)
    capacity_m3: Optional[float] = Field(None, gt=0)
    has_refrigerator: Optional[bool] = None
    vehicle_type: Optional[str] = Field(None, min_length=1)
    is_verified: Optional[bool] = None
    current_status: Optional[str] = Field(None, min_length=1)
    rating_completed_trips: Optional[int] = Field(None, ge=0)
    rating_failed_trips: Optional[int] = Field(None, ge=0)
