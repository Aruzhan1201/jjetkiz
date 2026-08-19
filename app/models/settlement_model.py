import uuid

from sqlalchemy import Column, Float, String, Uuid
from .user_model import Base


class Settlement(Base):
    __tablename__ = "settlements"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
