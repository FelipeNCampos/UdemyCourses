from flask import Flask 
from app.backend.config import Config

from app.backend.database import db

def create_backend_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)


    from app.backend.models import models

    with app.app_context():
        db.create_all()

    from app.backend.routes import register_routes

    register_routes(app)

    return app  

