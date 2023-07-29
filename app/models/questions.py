# import db object from app.extensions
from app.extensions import db

# model Question that uses db.Model class
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    answer = db.Column(db.Text)

    # string representation for each question using it's content
    def __repr__(self):
        return f'<Question {self.content}>'