from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


db = SQLAlchemy()
login_manager = LoginManager()


def user_login(user):
    login_user(user)


def user_logout():
    logout_user()


def get_current_user():
    return current_user



