# app/routers/__init__.py

from app.routes.users import users_bp


def register_routes(app):
    app.register_blueprint(users_bp, url_prefix="/api")
