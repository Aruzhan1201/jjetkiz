from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class OrderStatusHistorySchema(BaseModel):
    id: UUID
    order_id: UUID
    status: str = Field(..., min_length=1)
    changed_at: datetime
    changed_by_user_id: Optional[UUID] = None

    class Config:
        from_attributes = True

class OrderStatusHistoryCreate(BaseModel):
    order_id: UUID
    status: str = Field(..., min_length=1)
    changed_by_user_id: Optional[UUID] = None
