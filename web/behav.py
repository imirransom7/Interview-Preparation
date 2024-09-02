from flask import Blueprint, render_template
from questions_data.behavioral_questions import behavioral_questions

behav = Blueprint('behav', __name__)

@behav.route('/behav')
def behavioral():
    return render_template('behav.html', questions=behavioral_questions['question'])