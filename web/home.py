from flask import Blueprint
from flask import render_template

# defining this file as the blueprint of the application
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('')