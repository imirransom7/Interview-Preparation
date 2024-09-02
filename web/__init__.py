from config import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

# adding this line to tell SQLAlchemy to use PyMySQL instead of MySQLdb()
pymysql.install_as_MySQLdb()
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

    # importing blueprints
    from .views import views
    from .tech import tech
    from .behav import behav

    # registering blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(tech, url_prefix='/')
    app.register_blueprint(behav)

    with app.app_context():
        db.create_all()

    return app