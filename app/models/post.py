# import the database object
from app.extensions import db

# Flask-SQLAlchemy db model that takes db.Model as parameter
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    # string representation for each post object using its title
    def __repr__(self):
        return f'<Post "{self.title}">'