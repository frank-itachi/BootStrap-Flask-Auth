from flask import Blueprint, render_template, request, redirect, url_for, flash 
from forms import Login, Register
from extensions import db
from models import User

route = Blueprint('route', __name__)


@route.route('/')
def index():
    db.create_all()
    user_name =  request.args.get("user_name")
    return render_template("index.html", user=user_name)


@route.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Login(request.form)
    msg = "User or password incorrect. Please try again."
    if request.method == "POST" and login_form.validate():
        user = User.query.filter_by(email=str(login_form.email.data)).first()
        if not user:
            flash(msg)
            return redirect('/login')
        elif user.password != str(login_form.password.data):
            flash(msg)
            return redirect('/login')
        else:
            return redirect(url_for('route.index', user_name=user.first_name))
        
    return render_template("login.html", form=login_form)


@route.route('/register', methods=['GET', 'POST'])
def register():
    register_form = Register(request.form)
    if request.method == "POST" and register_form.validate():
        user = User.query.filter_by(email=str(register_form.user_email.data)).first()
        if not user:
            user = User()
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
            flash("An account already exists with this email.")
            return render_template("signup.html", form=register_form)
        
    return render_template("signup.html", form=register_form)


