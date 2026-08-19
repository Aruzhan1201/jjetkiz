import uuid

from sqlalchemy import Column, String, Uuid
from .user_model import Base


class CustomerProfile(Base):
    __tablename__ = "customer_profiles"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id = Column(Uuid, nullable=False, unique=True)
    company_name = Column(String(255), nullable=True)
    settlement = Column(String(100), nullable=False)
    business_type = Column(String(50), nullable=False)
