from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.calculations import Calculations


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid login credentials')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('results')
        flash('Thanks for logging in {}!'.format(current_user.username))
        return redirect(next_page)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        user = User.query.filter_by(username=register_form.username.data.lower()).first()
        if user:
            register_form.username.errors.append('Username taken')
            return redirect('register')
        user = User(username=register_form.username.data.lower(), email=register_form.email.data.lower(), age=register_form.age.data, salary=register_form.salary.data)
        calc = Calculations(register_form.age.data, register_form.salary.data)
        user.set_password(register_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! You can now view your retirement info.')
        return redirect(url_for('login'))
    return render_template('register.html', form=register_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
    return render_template("profile.html", title='Profile')


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data.lower()
        current_user.email = form.email.data.lower()
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    return render_template('edit_profile.html', title='Edit Profile', form=form)

@login_required
@app.route('/results', methods=['GET', 'POST'])
def results():
    calc = Calculations(current_user.age, current_user.salary)
    return render_template('results.html', calc=calc, title='Results')
