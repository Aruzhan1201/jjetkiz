from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class WeatherSnapshotSchema(BaseModel):
    id: UUID
    region_point_lat: float
    region_point_lng: float
    temperature_c: float
    wind_speed_ms: float = Field(..., ge=0)
    is_dust_storm_risk: bool = False
    fetched_at: datetime
    raw_response: Optional[dict] = None

    class Config:
        from_attributes = True

class WeatherSnapshotCreate(BaseModel):
    region_point_lat: float
    region_point_lng: float
    temperature_c: float
    wind_speed_ms: float = Field(..., ge=0)
    is_dust_storm_risk: bool = False
    fetched_at: datetime = Field(default_factory=datetime.utcnow)
