import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:your_new_password@localhost/bus_booking'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False