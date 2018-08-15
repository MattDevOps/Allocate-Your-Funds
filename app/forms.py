from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError, NumberRange, InputRequired
from app.models import User
from app.calculations import Calculations

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

    def check_for_invalid(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('That username doesn\'t exist.')


class RegistrationForm(FlaskForm):
    username = StringField('Username*', validators=[Length(min=6, max=24), DataRequired()])
    full_name = StringField('Full Name*', validators=[Length(min=1, max=34), DataRequired()])
    age = IntegerField('How old are you?*', validators=[InputRequired(),NumberRange(min=0, max=99999999, message="Input is not a number")])
    salary = IntegerField('What is your yearly salary?', validators=[InputRequired(),NumberRange(min=0, max=99999999, message="Input is not a number")])
    risk = IntegerField('Please enter a risk level from 1-5?*', validators=[DataRequired()])
    email = StringField('Email Address*', validators=[DataRequired(), Email()])
    password = PasswordField('Password*', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password*', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')

    def validate_risk(form, risk):
        if risk.data > 5:
            flash('You did not enter a valid risk level')
            raise ValidationError('Please enter a valid risk level')

    def validate_age(form, age):
        if isinstance(age.data, int) == False:
            flash('You did not enter a valid age')
            raise ValidationError('Please enter numbers only')

    def validate_salary(form, salary):
        if isinstance(salary.data, int) == False:
            flash('You did not enter a valid salary')
            raise ValidationError('Please enter numbers only')

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
    full_name = StringField('Full Name', validators=[Length(min=1, max=34)])
    age = IntegerField('How old are you?')
    salary = IntegerField('What is your yearly salary?')
    risk = IntegerField('Please enter a risk level 1-5')
    password = PasswordField('Password')
    password2 = PasswordField('Confirm Password', validators=[EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')

    def validate_risk(form, risk):
        if risk.data > 5:
            flash('You did not enter a valid risk level')
            raise ValidationError('Please enter a valid risk level')

    #this replaces the need for a jinja2 implementation
    def validate_age(form, age):
        if isinstance(age.data, int) == False:
            flash('You did not enter a valid age')
            raise ValidationError('Please enter numbers only')

    #this replaces the need for a jinja2 implementation
    def validate_salary(form, salary):
        if isinstance(salary.data, int) == False:
            flash('You did not enter a valid salary')
            raise ValidationError('Invalid salary')

    #overwritten in jinja2 on edit_profile.html
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Username taken')
            raise ValidationError('Username already taken.')

    #overwritten in jinja2 on edit_profile.html
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already in use')
            raise ValidationError('Email already taken.')
