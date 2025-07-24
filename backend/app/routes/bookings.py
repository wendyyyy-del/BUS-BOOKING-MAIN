from flask import Blueprint, request, jsonify
from ..models import db, Booking, Bus

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/', methods=['POST'])
def create_booking():
    data = request.json
    bus = Bus.query.get(data['bus_id'])
    if not bus:
        return jsonify({'error': 'Bus not found'}), 404
    # Check if seat is already booked
    if Booking.query.filter_by(bus_id=bus.id, seat_number=data['seat_number']).first():
        return jsonify({'error': 'Seat already booked'}), 400
    booking = Booking(
        bus_id=bus.id,
        seat_number=data['seat_number'],
        name=data['name'],
        id_number=data['id_number'],
        school_id=data.get('school_id'),
        phone=data['phone']
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({'message': 'Booking successful', 'booking_id': booking.id})