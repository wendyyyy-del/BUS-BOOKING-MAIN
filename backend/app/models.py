from . import db

class Bus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    from_location = db.Column(db.String(80), nullable=False)
    to_location = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    price_per_seat = db.Column(db.Float, nullable=False)
    route = db.Column(db.String(120), nullable=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.id'))
    seat_number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    id_number = db.Column(db.String(20), nullable=False)
    school_id = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.String(20), nullable=False)