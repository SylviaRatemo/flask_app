from flask import render_template, request, url_for, redirect
from app.questions import bp
from app.models.questions import Question
from app.extensions import db

# pass the ('GET', 'POST") tuple to methods parameter, allowing the two methodss
@bp.route('/', methods=('GET', 'POST'))
def index():
    questions = Question.query.all()

    if request.method == 'POST':
        # Question object created using content and answer submitted (request.form)
        new_question = Question(content=request.form['content'], answer=request.form['answer'])
        # add the new question to the db session
        db.session.add(new_question)
        # commit the transaction
        db.session.commit()
        # reditect user to questions index page
        print('Submitted')
        return redirect(url_for('questions.index'))
    
    return render_template("questions/index.html", questions=questions)