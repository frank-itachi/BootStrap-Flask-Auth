from wtforms import Form, EmailField, PasswordField
from wtforms.validators import DataRequired


class Login(Form):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
