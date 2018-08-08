from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

    def check_for_invalid(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('That username does exist.')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=6, max=24), DataRequired()])
    full_name = StringField('Full Name', validators=[Length(min=1, max=34), DataRequired()])
    age = IntegerField('How old are you?', validators=[DataRequired()])
    salary = IntegerField('What is your gross salary?', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Username taken')
            raise ValidationError('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already in use')
            raise ValidationError('Email already taken.')


class EditProfileForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email Address', validators=[Email()])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Username taken')
            raise ValidationError('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already in use')
            raise ValidationError('Email already taken.')
