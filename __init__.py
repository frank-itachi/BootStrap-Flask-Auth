from flask import Flask
from routes import route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(route)

    return app


flask_app = create_app()

if __name__ == "__main__":
    flask_app.run(debug=True)

