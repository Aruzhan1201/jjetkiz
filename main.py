import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import *
from app.routers import users_router, driver_profiles_router, customer_profiles_router, \
    orders_router, order_offers_router, ltl_groups_router, order_status_history_router, \
    tracking_points_router, weather_snapshots_router, refresh_tokens_router, settlements_router
from app.db.session import get_db_session
from sqlalchemy.orm import Session

# Create database tables on startup
from app.models import Base, User, Settlement, DriverProfile, CustomerProfile, Order, \
    OrderStatusHistory, OrderOffer, LtlGroup, TrackingPoint, WeatherSnapshot, RefreshToken
from app.db.base import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Freight Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Freight Management API", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# Include all API routers
app.include_router(users_router)
app.include_router(driver_profiles_router)
app.include_router(customer_profiles_router)
app.include_router(orders_router)
app.include_router(order_offers_router)
app.include_router(ltl_groups_router)
app.include_router(order_status_history_router)
app.include_router(tracking_points_router)
app.include_router(weather_snapshots_router)
app.include_router(refresh_tokens_router)
app.include_router(settlements_router)


def get_db():
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
