from flask import Blueprint, jsonify, request
from models import Order, User
from flask_jwt_extended import jwt_required, get_jwt_identity

routes = Blueprint("routes", __name__)

# IDOR Vulnerability: Does not check if order.user_id == current_user
@routes.route("/api/orders/<int:order_id>")
@jwt_required()
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "not found"}), 404

    return jsonify({
        "order_id": order.id,
        "item": order.item,
        "user_id": order.user_id
    })

# Horizontal Privilege Escalation: Access any user profile
@routes.route("/api/profile/<int:user_id>")
@jwt_required()
def profile(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "not found"}), 404

    return jsonify({
        "user_id": user.id,
        "username": user.username,
        "role": user.role
    })

# Vertical Privilege Escalation: This endpoint is completely unprotected
@routes.route("/admin/all_orders", methods=["GET"])
def all_orders():
    orders = Order.query.all()
    return jsonify([
        {"order_id": o.id, "item": o.item, "user_id": o.user_id}
        for o in orders
    ])