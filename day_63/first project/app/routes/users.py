from flask import Blueprint, request, jsonify
from app.database import db
from app.models import User

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json

    user = User(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201




@users_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(users_list), 200



@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200


    