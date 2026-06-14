from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Book

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=["POST"])
def create_book():
    data = request.json

    book = Book(
        title=data["title"],
        author=data["author"],
        rating=data["rating"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book created successfully"}), 201




@books_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    books_list = [{"id": book.id, "title": book.title, "author": book.author, "rating": book.rating} for book in books]
    return jsonify(books_list), 200



@books_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({"id": book.id, "title": book.title, "author": book.author, "rating": book.rating}), 200

@books_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.rating = data.get("rating", book.rating)

    db.session.commit()

    return jsonify({"message": "Book updated successfully"}), 200

@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully"}), 200