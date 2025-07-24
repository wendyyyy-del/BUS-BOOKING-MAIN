from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS  # <-- Add this line

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)  # <-- Add this line

    # Import and register blueprints inside the function, not at the top!
    from .routes.buses import buses_bp
    from .routes.bookings import bookings_bp
    app.register_blueprint(buses_bp, url_prefix='/api/buses')
    app.register_blueprint(bookings_bp, url_prefix='/api/bookings')

    return app