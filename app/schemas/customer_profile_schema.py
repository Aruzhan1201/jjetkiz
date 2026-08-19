from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class CustomerProfileSchema(BaseModel):
    id: UUID
    user_id: UUID
    company_name: Optional[str] = Field(None, max_length=255)
    settlement: str = Field(..., min_length=1, max_length=100)
    business_type: str = Field(..., min_length=1, max_length=50)

    class Config:
        from_attributes = True

class CustomerProfileCreate(BaseModel):
    user_id: UUID
    company_name: Optional[str] = Field(None, max_length=255)
    settlement: str = Field(..., min_length=1, max_length=100)
    business_type: str = Field(..., min_length=1, max_length=50)

class CustomerProfileUpdate(BaseModel):
    company_name: Optional[str] = Field(None, max_length=255)
    settlement: Optional[str] = Field(None, min_length=1, max_length=100)
    business_type: Optional[str] = Field(None, min_length=1, max_length=50)
