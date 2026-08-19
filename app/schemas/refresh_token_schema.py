from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class RefreshTokenSchema(BaseModel):
    id: UUID
    user_id: UUID
    token_hash: str = Field(..., min_length=1, max_length=255)
    expires_at: datetime
    revoked_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class RefreshTokenCreate(BaseModel):
    user_id: UUID
    token_hash: str = Field(..., min_length=1, max_length=255)
    expires_at: datetime = Field(..., gt=datetime.utcnow())

class RefreshTokenUpdate(BaseModel):
    revoked_at: Optional[datetime] = None
