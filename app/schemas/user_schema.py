from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class UserSchema(BaseModel):
    id: UUID
    phone: str = Field(..., min_length=1, max_length=20)
    role: str = Field(..., min_length=1)
    full_name: str = Field(..., min_length=1, max_length=255)
    created_at: datetime
    is_active: bool
    profile_status: str = Field(..., min_length=1)

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    phone: str = Field(..., min_length=1, max_length=20)
    role: str = Field(default="customer", min_length=1)
    full_name: str = Field(..., min_length=1, max_length=255)
    is_active: bool = True
    profile_status: str = Field(default="incomplete", min_length=1)

class UserUpdate(BaseModel):
    phone: Optional[str] = Field(None, min_length=1, max_length=20)
    role: Optional[str] = Field(None, min_length=1)
    full_name: Optional[str] = Field(None, min_length=1, max_length=255)
    is_active: Optional[bool] = None
    profile_status: Optional[str] = Field(None, min_length=1)
