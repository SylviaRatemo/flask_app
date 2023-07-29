# posts blueprint
from flask import Blueprint

# create blueprint object
bp = Blueprint('posts', __name__)

# import routes
from app.posts import routes