

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'flask_db'
DB_USER = 'postgres'
DB_PASS = '1234'

DEBUG = True

SECRET_KEY = "my_precious"
SECURITY_PASSWORD_SALT = "my_precious_two"

# Database connection string.
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

# http://flask-sqlalchemy.pocoo.org/2.3/config/
SQLALCHEMY_TRACK_MODIFICATIONS = False