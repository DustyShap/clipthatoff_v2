import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from dotenv import load_dotenv
from clipthatoff.models import db


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    Bootstrap(app)
    return app

def main():
    db.create_all()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        main()
