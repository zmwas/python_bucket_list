from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SelectField
from wtforms.validators import Email, InputRequired


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    email = StringField('email', validators=[Email()])
    password = PasswordField('password')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = PasswordField('password', validators=[InputRequired()])


class CreateBucketListForm(FlaskForm):
    bucket_name = StringField('Bucket Name ', validators=[InputRequired()])


class CreateBucketItemForm(FlaskForm):
    bucket_item_name = StringField('Bucket list item ', validators=[InputRequired()])


class UpdateBucketListForm(FlaskForm):
    bucket_name = StringField('Bucket Name ', validators=[InputRequired()])
    completion_status = SelectField(u'Status', choices=[('Completed,Completed'), ('In Progress', 'In Progress'),
                                                        ('On Ice', 'On Ice')])


class UpdateBucketListForm(FlaskForm):
    bucket_item_name = StringField('Bucket list item ', validators=[InputRequired()])
    completion_status = SelectField(u'Status', choices=[('Completed,Completed'), ('In Progress', 'In Progress'),
                                                        ('On Ice', 'On Ice')])
