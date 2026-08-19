from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from enum import Enum

class OrderStatus(str, Enum):
    created = "created"
    matching = "matching"
    offered = "offered"
    accepted = "accepted"
    in_progress = "in_progress"
    delivered = "delivered"
    cancelled = "cancelled"
    expired = "expired"

class PackagingQuality(str, Enum):
    good = "good"
    acceptable = "acceptable"
    poor = "poor"

class OrderSchema(BaseModel):
    id: UUID
    customer_id: UUID
    status: OrderStatus = Field(default="created")
    point_a_lat: float = Field(..., gt=0)
    point_a_lng: float = Field(..., gt=0)
    point_a_address: str = Field(..., min_length=1, max_length=500)
    point_b_lat: float = Field(..., gt=0)
    point_b_lng: float = Field(..., gt=0)
    point_b_address: str = Field(..., min_length=1, max_length=500)
    cargo_weight_kg: float = Field(..., gt=0)
    cargo_volume_m3: float = Field(..., gt=0)
    is_perishable: bool = False
    is_fragile: bool = False
    packaging_quality: Optional[PackagingQuality] = None
    packaging_photo_url: Optional[str] = Field(None, max_length=500)
    cargo_description: Optional[str] = Field(None)
    priority_level: str = Field(default="normal", min_length=1)
    is_social_priority: bool = False
    weather_delay_warning: bool = False
    estimated_delivery_minutes: Optional[float] = Field(None, gt=0)
    requested_pickup_time: Optional[str] = Field(None)
    price_offer: Optional[float] = Field(None, gt=0)
    assigned_driver_id: Optional[UUID] = None
    is_ltl_group: bool = False
    ltl_group_id: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    customer_id: UUID
    status: Optional[OrderStatus] = Field(default="created")
    point_a_lat: float = Field(..., gt=0)
    point_a_lng: float = Field(..., gt=0)
    point_a_address: str = Field(..., min_length=1, max_length=500)
    point_b_lat: float = Field(..., gt=0)
    point_b_lng: float = Field(..., gt=0)
    point_b_address: str = Field(..., min_length=1, max_length=500)
    cargo_weight_kg: float = Field(..., gt=0)
    cargo_volume_m3: float = Field(..., gt=0)
    is_perishable: bool = False
    is_fragile: bool = False
    packaging_quality: Optional[PackagingQuality] = None
    packaging_photo_url: Optional[str] = Field(None, max_length=500)
    cargo_description: Optional[str] = Field(None)
    priority_level: str = Field(default="normal", min_length=1)
    is_social_priority: bool = False
    weather_delay_warning: bool = False
    estimated_delivery_minutes: Optional[float] = Field(None, gt=0)
    requested_pickup_time: Optional[str] = Field(None)
    price_offer: Optional[float] = Field(None, gt=0)
    assigned_driver_id: Optional[UUID] = None
    is_ltl_group: bool = False
    ltl_group_id: Optional[UUID] = None

class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None
    assigned_driver_id: Optional[UUID] = None
    is_ltl_group: Optional[bool] = None
    ltl_group_id: Optional[UUID] = None
    estimated_delivery_minutes: Optional[float] = Field(None, gt=0)
    price_offer: Optional[float] = Field(None, gt=0)
