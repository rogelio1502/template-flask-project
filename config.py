import os

SECRET_KEY = os.urandom(32)

#Grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

#Enable debug mode
DEBUG = True

# Connect to the database 
#our database url
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False