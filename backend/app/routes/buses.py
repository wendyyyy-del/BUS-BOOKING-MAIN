from flask import Blueprint, jsonify
from ..models import Bus, Booking

buses_bp = Blueprint('buses', __name__)

@buses_bp.route('/', methods=['GET'])
def get_buses():
    buses = Bus.query.all()
    return jsonify([
        {
            'id': b.id,
            'name': b.name,
            'from_location': b.from_location,
            'to_location': b.to_location,
            'date': b.date,
            'time': b.time,
            'seats': b.seats,
            'price_per_seat': b.price_per_seat
        } for b in buses
    ])

@buses_bp.route('/<int:bus_id>/seats', methods=['GET'])
def get_booked_seats(bus_id):
    bookings = Booking.query.filter_by(bus_id=bus_id).all()
    return jsonify([b.seat_number for b in bookings])