from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, TextAreaField, SelectField, PasswordField
from wtforms.validators import InputRequired, Email, Optional, URL, Length, NumberRange

class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    email = StringField('E-mail', validators=[InputRequired(), Email()])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=7, max=30)])


class BreedForm(FlaskForm):
    breed = StringField("Title", validators=[InputRequired(), Length(min=2, max=25)])


class DeleteForm(FlaskForm):
    """Delete form."""
