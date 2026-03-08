from flask import Flask
from database import db
from auth import auth
from routes import routes
from models import User, Order
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "secretkey"

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

    if not User.query.first():
        user1 = User(username="alice", password="123", role="user")
        user2 = User(username="bob", password="123", role="user")
        admin = User(username="admin", password="admin", role="admin")

        db.session.add_all([user1, user2, admin])
        db.session.commit()

        order1 = Order(item="Laptop", user_id=1)
        order2 = Order(item="Phone", user_id=2)
        order3 = Order(item="Tablet", user_id=2)

        db.session.add_all([order1, order2, order3])
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)