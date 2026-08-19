from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class SettlementSchema(BaseModel):
    id: UUID
    name: str = Field(..., min_length=1, max_length=100)
    lat: float
    lng: float

    class Config:
        from_attributes = True

class SettlementCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    lat: float
    lng: float

class SettlementUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    lat: Optional[float] = None
    lng: Optional[float] = None
