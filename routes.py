from flask import Blueprint, render_template
from forms import Login, Register

route = Blueprint('route', __name__)


@route.route('/')
def index():
    return render_template("index.html")


@route.route('/login')
def login():
    login_form = Login()
    return render_template("login.html", form=login_form)


@route.route('/register')
def register():
    register_form = Register()
    return render_template("signup.html", form=register_form)


