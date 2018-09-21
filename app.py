from flask import Flask, render_template, redirect, url_for, session
from forms import LoginForm, RegistrationForm
from models import User, db
from create import create_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = create_app()
app.app_context().push()


@app.route('/')
def index():
    logged_in_email = session.get('logged_in_email')
    if logged_in_email:
        return render_template('index.html', email=logged_in_email)
    return render_template('index.html')


@app.route('/login', methods=['GET',  'POST'])
def login():
    if session['logged_in_email']:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                session['logged_in_email'] = user.email
                print(session['logged_in_email'])
                return redirect(url_for('index'))
    return render_template('login.html', form=form, error_message=error_message)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if session['logged_in_email']:
        return redirect(url_for('index'))
    error_message = ""
    form = RegistrationForm()
    if form.validate_on_submit():
        if not check_user_exist(form.email.data):
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            session['logged_in_email'] = form.email.data
            return redirect(url_for('index'))
        error_message = 'User already exists!'
    return render_template('signup.html', form=form, error_message=error_message)


@app.route('/logout')
def logout():
    session.pop('logged_in_email', None)
    return redirect(url_for('index'))


def check_user_exist(email):
    return User.query.filter_by(email=email).first()


#
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')
