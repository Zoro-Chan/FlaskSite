from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from FlaskSite.models import User

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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValueError('Username already taken.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValueError('Email already taken.')
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', 
    validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
    validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')