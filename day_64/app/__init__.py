from flask import Flask
from flask_bootstrap import Bootstrap5

from app.backend.config import Config
from app.backend.database import db

bootstrap = Bootstrap5()


def create_app():
    app = Flask(
        __name__,
        template_folder="frontend/templates",
        static_folder="frontend/static",
    )
    app.config.from_object(Config)

    db.init_app(app)
    bootstrap.init_app(app)

    from app.backend.models import models

    with app.app_context():
        db.create_all()

    from app.backend.routes import register_routes
    from app.frontend import frontend_bp

    register_routes(app)
    app.register_blueprint(frontend_bp)

    return app


