from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from app.backend.models import Movie
from app.backend.database import db


movies_bp = Blueprint("movies", __name__)


@movies_bp.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": error.description}), 400


def movie_to_dict(movie):
    return {
        "id": movie.id,
        "title": movie.title,
        "year": movie.year,
        "description": movie.description,
        "rating": movie.rating,
        "ranking": movie.ranking,
        "review": movie.review,
        "img_url": movie.img_url,
    }


def get_request_data():
    data = request.get_json(silent=True)

    if data is None and request.form:
        data = request.form.to_dict()

    if not data:
        raise BadRequest("Send the movie data as JSON or form data.")

    return data


def parse_int(value, field_name, required=False):
    if value in (None, ""):
        if required:
            raise BadRequest(f"{field_name} is required.")
        return None

    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise BadRequest(f"{field_name} must be an integer.") from exc


def parse_float(value, field_name):
    if value in (None, ""):
        return None

    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise BadRequest(f"{field_name} must be a number.") from exc


@movies_bp.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    # Placeholder for fetching a specific movie by ID from the database
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie_to_dict(movie))


@movies_bp.route("/movies", methods=["GET"])
def get_movies():
    # Placeholder for fetching movies from the database
    movies = Movie.query.all()
    return jsonify([movie_to_dict(movie) for movie in movies])


@movies_bp.route("/movies", methods=["POST"])
def add_movie():
    data = get_request_data()

    if not data.get("title"):
        raise BadRequest("title is required.")

    # Placeholder for adding a new movie to the database
    new_movie = Movie(
        title=data.get("title"),
        year=parse_int(data.get("year"), "year", required=True),
        description=data.get("description"),
        rating=parse_float(data.get("rating"), "rating"),
        ranking=parse_int(data.get("ranking"), "ranking"),
        review=data.get("review"),
        img_url=data.get("img_url"),
    )

    try:
        db.session.add(new_movie)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A movie with this title already exists."}), 409

    return jsonify(movie_to_dict(new_movie)), 201


@movies_bp.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = get_request_data()
    # Placeholder for updating a specific movie by ID in the database
    movie = Movie.query.get_or_404(movie_id)
    movie.title = data.get("title", movie.title)

    if "year" in data:
        movie.year = parse_int(data.get("year"), "year", required=True)

    movie.description = data.get("description", movie.description)

    if "rating" in data:
        movie.rating = parse_float(data.get("rating"), "rating")

    if "ranking" in data:
        movie.ranking = parse_int(data.get("ranking"), "ranking")

    movie.review = data.get("review", movie.review)
    movie.img_url = data.get("img_url", movie.img_url)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "A movie with this title already exists."}), 409

    return jsonify(movie_to_dict(movie))


@movies_bp.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    # Placeholder for deleting a specific movie by ID from the database
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Movie deleted successfully"})
