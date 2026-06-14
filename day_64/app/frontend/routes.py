from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError

from app.backend.database import db
from app.backend.models import Movie
from app.frontend.forms import MovieForm


frontend_bp = Blueprint("frontend", __name__)


def parse_int(value, field_name, required=False):
    if value in (None, ""):
        if required:
            raise ValueError(f"{field_name} is required.")
        return None

    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{field_name} must be an integer.") from exc


def parse_float(value, field_name):
    if value in (None, ""):
        return None

    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"{field_name} must be a number.") from exc


def movie_from_form(movie):
    movie.title = request.form.get("title", "").strip()
    movie.year = parse_int(request.form.get("year"), "year", required=True)
    movie.description = request.form.get("description", "").strip() or None
    movie.rating = parse_float(request.form.get("rating"), "rating")
    movie.ranking = parse_int(request.form.get("ranking"), "ranking")
    movie.review = request.form.get("review", "").strip() or None
    movie.img_url = request.form.get("img_url", "").strip() or None

    if not movie.title:
        raise ValueError("title is required.")

    return movie


@frontend_bp.route("/")
def home():
    movies = Movie.query.order_by(Movie.ranking.is_(None), Movie.ranking).all()
    total_movies = len(movies)

    if total_movies == 0:
        return render_template("index.html", movie=None)

    position = request.args.get("position", 1, type=int)
    position = max(1, min(position, total_movies))
    movie = movies[position - 1]
    previous_position = total_movies if position == 1 else position - 1
    next_position = 1 if position == total_movies else position + 1

    return render_template(
        "index.html",
        movie=movie,
        position=position,
        total_movies=total_movies,
        previous_position=previous_position,
        next_position=next_position,
    )


@frontend_bp.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        try:
            movie = movie_from_form(Movie())
            db.session.add(movie)
            db.session.commit()
            flash("Movie added successfully.", "success")
            return redirect(url_for("frontend.home"))
        except ValueError as error:
            flash(str(error), "danger")
        except IntegrityError:
            db.session.rollback()
            flash("A movie with this title already exists.", "danger")

    return render_template("add.html")


@frontend_bp.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = MovieForm(obj=movie)

    if form.validate_on_submit():
        try:
            form.populate_obj(movie)
            db.session.commit()
            flash("Movie updated successfully.", "success")
            return redirect(url_for("frontend.home"))
        except IntegrityError:
            db.session.rollback()
            flash("A movie with this title already exists.", "danger")

    return render_template("edit.html", movie=movie, form=form)


@frontend_bp.route("/delete/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("Movie deleted successfully.", "success")
    return redirect(url_for("frontend.home"))


@frontend_bp.route("/select")
def select_movie():
    movies = Movie.query.order_by(Movie.title).all()
    return render_template("select.html", movies=movies)
