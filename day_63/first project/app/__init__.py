from flask import Flask 
from app.config import Config

from app.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)


    from app import models 

    with app.app_context():
        db.create_all()

    from app.routes import register_routes

    register_routes(app)

    return app  

