from config import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# initializing database
db = SQLAlchemy()

# Initializing Flask
def create_app():
    app = Flask(__name__)
    # Securing rhe cookies session data; the secret key for the application
    app.config["SECRET_KEY"] = secret_key
    # Storing the database inside the web folder
    app.config['SQLALCHEMY_DATABASE_URI'] = mysql_path
    # turning tracking off
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # taking the database and telling it this is the app we are going to use
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app