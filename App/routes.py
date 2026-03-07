from flask import Blueprint, jsonify
from models import Order

routes = Blueprint("routes", __name__)


# IDOR vulnerability
@routes.route("/api/orders/<int:order_id>")
def get_order(order_id):

    order = Order.query.get(order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    return jsonify({
        "order_id": order.id,
        "item": order.item,
        "user_id": order.user_id
    })


# admin endpoint without access check
@routes.route("/admin/all_orders")
def all_orders():

    orders = Order.query.all()

    data = []

    for o in orders:
        data.append({
            "order_id": o.id,
            "item": o.item,
            "user_id": o.user_id
        })

    return jsonify(data)