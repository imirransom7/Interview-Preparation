from flask import Blueprint, render_template

tech = Blueprint('tech', __name__)

@tech.route('/tech')
def tech_cards():
    render_template('tech.html')