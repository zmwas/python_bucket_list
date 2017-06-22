from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import Email


class RegistrationForm(FlaskForm):
    name = StringField('name')
    email = StringField('email', validators=[Email()])
    password = PasswordField('password')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = PasswordField('password')



