from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class JoinForm(FlaskForm):
    username = StringField('Username', 
    validators=[DataRequired(), Length(min=3, max=15)])

    email = StringField('Email', 
    validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
    validators=[DataRequired()])

    confirm_password = PasswordField('Retype Password', 
    validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('I Accept the RULES and I wanted to JOIN!')


class LoginForm(FlaskForm):
    email = StringField('Email', 
    validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
    validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')