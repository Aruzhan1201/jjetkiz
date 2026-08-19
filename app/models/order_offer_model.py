import uuid

from sqlalchemy import Column, DateTime, Enum, Uuid
from .enums import offer_status_enum
from .user_model import Base


class OrderOffer(Base):
    __tablename__ = "order_offers"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    order_id = Column(Uuid, nullable=True)
    ltl_group_id = Column(Uuid, nullable=True)
    driver_id = Column(Uuid, nullable=False)
    status = Column(offer_status_enum, nullable=False, default="sent")
    sent_at = Column(DateTime(timezone=True), nullable=False)
    responded_at = Column(DateTime(timezone=True), nullable=True)
