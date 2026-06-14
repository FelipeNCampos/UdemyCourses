from app.backend.routes.movies import movies_bp


def register_routes(app):
    app.register_blueprint(movies_bp, url_prefix="/api")
