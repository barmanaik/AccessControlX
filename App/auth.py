from flask import Blueprint, request, jsonify
from models import User
from database import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(
        username=data["username"],
        password=data["password"],
        role="user"
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"})


@auth.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(
        username=data["username"],
        password=data["password"]
    ).first()

    if user:
        return jsonify({
            "message": "login successful",
            "user_id": user.id,
            "role": user.role
        })

    return jsonify({"error": "invalid credentials"}), 401