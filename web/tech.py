from flask import Blueprint, render_template
from questions_data.technical_questions import technical_questions

tech = Blueprint('tech', __name__)


@tech.route('/tech')
def tech_cards():
    return render_template('tech.html', questions=technical_questions['question'],
                           answers=technical_questions['answer'])