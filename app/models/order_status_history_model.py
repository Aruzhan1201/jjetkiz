import uuid

from sqlalchemy import Column, DateTime, Enum, Uuid
from .enums import order_status_enum
from .user_model import Base


class OrderStatusHistory(Base):
    __tablename__ = "order_status_history"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    order_id = Column(Uuid, nullable=False)
    status = Column(order_status_enum, nullable=False)
    changed_at = Column(DateTime(timezone=True), nullable=False)
    changed_by_user_id = Column(Uuid, nullable=True)
