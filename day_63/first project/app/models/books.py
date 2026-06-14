from app.database import db


class Book(db.Model):  # ty: ignore[unsupported-base]
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=True)