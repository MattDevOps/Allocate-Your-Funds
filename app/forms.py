from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError, NumberRange, InputRequired
from app.models import User

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
    salary = IntegerField('What is your salary?', validators=[InputRequired(),NumberRange(min=0, max=99999999, message="Input is not a number")])
    risk = StringField('Would you consider yourself a risky person?*', validators=[DataRequired(), ])
    email = StringField('Email Address*', validators=[DataRequired(), Email()])
    password = PasswordField('Password*', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password*', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')

    def validate_age(form, age):
        if isinstance(age.data, int) == False:
            flash('Please enter numbers only as your age')
            raise ValidationError('Please enter numbers only')

    def validate_salary(form, salary):
        if isinstance(salary.data, int) == False:
            flash('Please enter numbers only as your salary')
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
    salary = IntegerField('What is your gross salary?')
    risk = StringField('Would you consider yourself a risky person?')
    password = PasswordField('Password')
    password2 = PasswordField('Confirm Password', validators=[EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')

    def validate_age(form, age):
        if isinstance(age.data, int) == False:
            flash('Please enter numbers only as your age')
            raise ValidationError('Please enter numbers only')

    def validate_salary(form, salary):
        if isinstance(salary.data, int) == False:
            flash('Please enter numbers only as your salary')
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
