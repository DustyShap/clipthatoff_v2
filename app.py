from flask import Flask, render_template
from forms import LoginForm, RegistrationForm
from models import User, db
from create import create_app
from flask_sqlalchemy import SQLAlchemy


app = create_app()
app.app_context().push()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET',  'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return form.email.data + "," + form.password.data
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return 'New User Created'
    return render_template('signup.html', form=form)

# 
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')
