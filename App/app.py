from flask import Flask
from database import db
from auth import auth
from routes import routes
from models import User, Order

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(routes)


with app.app_context():
    db.create_all()

    if not User.query.first():

        user1 = User(username="alice", password="123", role="user")
        user2 = User(username="bob", password="123", role="user")

        db.session.add(user1)
        db.session.add(user2)

        db.session.commit()

        order1 = Order(item="Laptop", user_id=1)
        order2 = Order(item="Phone", user_id=2)

        db.session.add(order1)
        db.session.add(order2)

        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)