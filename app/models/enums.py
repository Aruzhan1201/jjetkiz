import sqlalchemy as sa


role_enum = sa.Enum("customer", "driver", "admin", name="role")
profile_status_enum = sa.Enum("incomplete", "complete", name="profile_status")
current_status_enum = sa.Enum("offline", "online", "on_order", name="current_status")
vehicle_type_enum = sa.Enum("tent", "flatbed", "pickup", "box_truck", name="vehicle_type")
order_status_enum = sa.Enum(
    "created", "matching", "offered", "accepted", "in_progress", "delivered",
    "cancelled", "expired", name="order_status"
)
priority_level_enum = sa.Enum("critical", "high", "normal", name="priority_level")
offer_status_enum = sa.Enum("sent", "accepted", "declined", "expired", name="offer_status")
packaging_quality_enum = sa.Enum("good", "acceptable", "poor", name="packaging_quality")
