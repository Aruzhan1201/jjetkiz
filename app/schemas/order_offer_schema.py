from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional
from uuid import UUID
from enum import Enum

class OfferStatus(str, Enum):
    sent = "sent"
    accepted = "accepted"
    declined = "declined"
    expired = "expired"

class OrderOfferSchema(BaseModel):
    id: UUID
    order_id: Optional[UUID] = None
    ltl_group_id: Optional[UUID] = None
    driver_id: UUID
    status: OfferStatus = Field(default="sent")
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    responded_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class OrderOfferCreate(BaseModel):
    order_id: Optional[UUID] = None
    ltl_group_id: Optional[UUID] = None
    driver_id: UUID
    status: OfferStatus = Field(default="sent")
    sent_at: datetime = Field(default_factory=datetime.utcnow)

    @validator("order_id", "ltl_group_id", pre=True, always=True)
    def check_exactly_one(cls, v, values):
        has_order = "order_id" in values
        has_ltl = "ltl_group_id" in values
        if has_order and has_ltl:
            raise ValueError("Exactly one of order_id or ltl_group_id required")
        if not has_order and not has_ltl:
            raise ValueError("Exactly one of order_id or ltl_group_id required")
        return v

class OrderOfferUpdate(BaseModel):
    status: Optional[OfferStatus] = None
    responded_at: Optional[datetime] = None
