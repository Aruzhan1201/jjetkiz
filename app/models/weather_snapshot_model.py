import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, JSON, String, Uuid
from .user_model import Base


class WeatherSnapshot(Base):
    __tablename__ = "weather_snapshots"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    region_point_lat = Column(Float, nullable=False)
    region_point_lng = Column(Float, nullable=False)
    temperature_c = Column(Float, nullable=False)
    wind_speed_ms = Column(Float, nullable=False)
    is_dust_storm_risk = Column(Boolean, default=False, nullable=False)
    fetched_at = Column(DateTime(timezone=True), nullable=False)
    raw_response = Column(JSON, nullable=True)
