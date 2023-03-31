from flask import Flask
from routes import route
from extensions import db
from models import *


def create_app():
    app = Flask(__name__)
    app.register_blueprint(route)

    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app


flask_app = create_app()

if __name__ == "__main__":
    flask_app.run(debug=True)

