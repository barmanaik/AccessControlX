from flask import Blueprint, request, jsonify
from models import User
from database import db
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(username=data["username"], password=data["password"], role="user")
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "user created"})

@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"], password=data["password"]).first()

    if user:
        # FIX: Include the 'role' in the token so students can practice manipulating it
        token = create_access_token(
            identity=str(user.id), 
            additional_claims={"role": user.role}
        )
        return jsonify(access_token=token)

    return jsonify({"msg": "invalid credentials"}), 401