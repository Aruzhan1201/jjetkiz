import sys
import os
from datetime import datetime, timezone

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.db.session import SessionLocal
from app.models import User, CustomerProfile, DriverProfile, Order

def seed_db():
    db = SessionLocal()
    
    # Clean up existing to prevent duplicates
    if db.query(User).count() > 0:
        print("Database already has users. Cleaning up first...")
        db.query(Order).delete()
        db.query(CustomerProfile).delete()
        db.query(DriverProfile).delete()
        db.query(User).delete()
        db.commit()
        
    print("Seeding database...")
    now = datetime.now(timezone.utc)
    
    # 1. Create Customer
    customer = User(
        phone="+77011234567",
        role="customer",
        full_name="Alice Customer",
        created_at=now,
        is_active=True,
        profile_status="approved"
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    
    customer_profile = CustomerProfile(
        user_id=customer.id,
        company_name="Alice Logistics",
        settlement="Aktau",
        business_type="B2B"
    )
    db.add(customer_profile)
    
    # 2. Create Driver
    driver = User(
        phone="+77029876543",
        role="driver",
        full_name="Bob Driver",
        created_at=now,
        is_active=True,
        profile_status="approved"
    )
    db.add(driver)
    db.commit()
    db.refresh(driver)
    
    driver_profile = DriverProfile(
        user_id=driver.id,
        vehicle_brand="Kamaz",
        vehicle_plate_number="123ABC12",
        capacity_kg=5000,
        capacity_m3=30,
        has_refrigerator=False,
        vehicle_type="truck",
        is_verified=True,
        current_status="online"
    )
    db.add(driver_profile)
    
    # 3. Create Orders
    order1 = Order(
        customer_id=customer.id,
        status="created",
        point_a_lat=43.6481,
        point_a_lng=51.1706,
        point_a_address="Aktau, Microdistrict 1",
        point_b_lat=43.2981,
        point_b_lng=52.8800,
        point_b_address="Zhanaozen, Microdistrict 2",
        cargo_weight_kg=1000,
        cargo_volume_m3=5.0,
        is_perishable=False,
        is_fragile=True,
        cargo_description="Electronics",
        priority_level="normal",
        created_at=now,
        updated_at=now,
        price_offer=15000.0,
    )
    
    order2 = Order(
        customer_id=customer.id,
        status="in_transit",
        assigned_driver_id=driver.id,
        point_a_lat=43.6481,
        point_a_lng=51.1706,
        point_a_address="Aktau Port",
        point_b_lat=43.8500,
        point_b_lng=50.3167,
        point_b_address="Fort-Shevchenko",
        cargo_weight_kg=2000,
        cargo_volume_m3=10.0,
        is_perishable=True,
        is_fragile=False,
        cargo_description="Fresh Fish",
        priority_level="high",
        created_at=now,
        updated_at=now,
        price_offer=25000.0,
    )
    
    db.add_all([order1, order2])
    db.commit()
    print("Seeding complete! You now have a customer, a driver, and some orders in the system.")
    
if __name__ == "__main__":
    seed_db()
