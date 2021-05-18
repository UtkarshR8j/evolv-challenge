import os
class Config(object):
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL') 