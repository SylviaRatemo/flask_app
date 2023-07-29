from app.posts import bp
from flask import render_template
# import db database object and Post model
from app.extensions import db
from app.models.post import Post

@bp.route('/')
def index():
    # get all the posts in the db
    posts = Post.query.all()
    # pass the posts from the db into the posts' index template
    return render_template('posts/index.html', posts=posts)

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')