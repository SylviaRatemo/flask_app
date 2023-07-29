# os module used to access the file system
import os

# establish the base directory to correctly set the path to the db file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # specifies the db to connect to using SQLAlchemy, either from DATABASE_URI envionment variable or default URI value, sqllite:///path/to/app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,'app.db')
    # disable tracking object modifications to use less memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False