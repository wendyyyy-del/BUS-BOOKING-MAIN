from app import create_app, db
from app.models import Bus

app = create_app()

with app.app_context():
    print("🧹 Clearing existing buses…")
    db.session.query(Bus).delete()
    db.session.commit()

    buses = [
    {
        "name": "JOHN WICK",
        "route": "Nairobi → Rongai",
        "from_location": "Nairobi",
        "to_location": "Rongai",
        "date": "2025-07-24",
        "time": "10:00",
        "seats": 30,
        "price_per_seat": 150,
    },
    {
        "name": "Mood",
        "route": "Nairobi → Embakasi",
        "from_location": "Nairobi",
        "to_location": "Embakasi",
        "date": "2025-07-25",
        "time": "12:00",
        "seats": 25,
        "price_per_seat": 100,
    },
    {
        "name": "Detroit 313",
        "route": "Nairobi → Rongai",
        "from_location": "Nairobi",
        "to_location": "Rongai",
        "date": "2025-07-26",
        "time": "14:00",
        "seats": 30,
        "price_per_seat": 150,
    },
    # Add more buses as needed...
]

    for b in buses:
        bus = Bus(**b)
        db.session.add(bus)

    db.session.commit()
    print("✅ Buses seeded!")