from flask import Blueprint
from flask import render_template

# defining this file as the blueprint of the application
home = Blueprint('home', __name__)

@home.route('/')
def views():
    return render_template('')