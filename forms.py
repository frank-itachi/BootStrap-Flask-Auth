from wtforms import Form, EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo


class Login(Form):
    email = EmailField(
        label='Email',
        validators=[DataRequired()],
        render_kw={"placeholder": "example@email.com"}
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired()],
        render_kw={"placeholder": "Your password"}
    )


class Register(Form):
    msg = "This field can not be empty."
    user_name = StringField(
        label='First Name',
        validators=[DataRequired(message=msg)],
        render_kw={"placeholder": "First Name"}
    )
    user_last_name = StringField(
        label='Last Name',
        validators=[DataRequired(message=msg)],
        render_kw={"placeholder": "Last Name"}
    )
    user_email = EmailField(
        label='Email',
        validators=[
            DataRequired(message=msg),
            Email(message="Please type a valid email.")
        ],
        render_kw={"placeholder": "example@email.com"}
    )
    user_password = PasswordField(
        label='Password',
        validators=[
            DataRequired(message=msg),
            EqualTo('confirm_password', message="Password must match.")
        ],
        render_kw={"placeholder": "Password"}
    )
    confirm_password = PasswordField(label='Confirm Password', render_kw={"placeholder": "Confirm Password"})
