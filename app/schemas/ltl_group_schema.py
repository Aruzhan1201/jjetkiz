from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class LtlGroupSchema(BaseModel):
    id: UUID
    status: str = Field(default="active", min_length=1)
    total_weight_kg: float = Field(default=0.0, ge=0)
    total_volume_m3: float = Field(default=0.0, ge=0)
    point_a_cluster_lat: float
    point_a_cluster_lng: float
    point_b_cluster_lat: float
    point_b_cluster_lng: float
    created_at: datetime

    class Config:
        from_attributes = True

class LtlGroupCreate(BaseModel):
    status: str = Field(default="active", min_length=1)
    total_weight_kg: float = Field(default=0.0, ge=0)
    total_volume_m3: float = Field(default=0.0, ge=0)
    point_a_cluster_lat: float
    point_a_cluster_lng: float
    point_b_cluster_lat: float
    point_b_cluster_lng: float

class LtlGroupUpdate(BaseModel):
    status: Optional[str] = Field(None, min_length=1)
    total_weight_kg: Optional[float] = Field(None, ge=0)
    total_volume_m3: Optional[float] = Field(None, ge=0)
    point_a_cluster_lat: Optional[float] = None
    point_a_cluster_lng: Optional[float] = None
    point_b_cluster_lat: Optional[float] = None
    point_b_cluster_lng: Optional[float] = None
