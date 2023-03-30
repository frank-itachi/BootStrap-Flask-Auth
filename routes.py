from flask import Blueprint, render_template, request, redirect
from forms import Login, Register
from extensions import db
from models import User

route = Blueprint('route', __name__)


@route.route('/')
def index():
    return render_template("index.html")


@route.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Login(request.form)
    if request.method == "POST" and login_form.validate():
        for attr in login_form:
            print(attr.data)
        return redirect('/')
    return render_template("login.html", form=login_form)


@route.route('/register', methods=['GET', 'POST'])
def register():
    register_form = Register(request.form)
    if request.method == "POST" and register_form.validate():
        user = User.query.filter_by(email=str(register_form.user_email.data)).first()
        if not user:
            user.first_name = str(register_form.user_name.data)
            user.last_name = str(register_form.user_last_name.data)
            user.email = str(register_form.user_email.data)
            user.password = str(register_form.user_password.data)
            print(user.first_name)
            # insert the user into the db
            db.session.add(user)
            db.session.commit()

            return redirect('/')
        else:
            pass
        return redirect('/')
    return render_template("signup.html", form=register_form)


