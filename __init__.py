from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
crud_db=SQLAlchemy(app)

import os
import pymysql
class Config(object):
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL') 
    