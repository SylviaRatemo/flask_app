# main blueprint, import Blueprint class
from flask import Blueprint

# create blueprint object, takes two arguments: the name, and __name__ variable(name of current Python module)
bp = Blueprint('main', __name__)

# import the routes in the blueprint to make them importable from here
from app.main import routes