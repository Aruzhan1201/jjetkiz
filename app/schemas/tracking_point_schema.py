from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class TrackingPointSchema(BaseModel):
    id: UUID
    driver_id: UUID
    order_id: Optional[UUID] = None
    lat: float = Field(..., gt=-90, lt=90)
    lng: float = Field(..., gt=-180, lt=180)
    recorded_at_device: datetime
    received_at_server: datetime
    created_at: datetime

    class Config:
        from_attributes = True

class TrackingPointCreate(BaseModel):
    driver_id: UUID
    order_id: Optional[UUID] = None
    lat: float = Field(..., gt=-90, lt=90)
    lng: float = Field(..., gt=-180, lt=180)
    recorded_at_device: datetime = Field(default_factory=datetime.utcnow)
    received_at_server: datetime = Field(default_factory=datetime.utcnow)
