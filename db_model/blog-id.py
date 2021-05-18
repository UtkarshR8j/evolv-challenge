from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields,Schema
crud_db=SQLAlchemy()

class blog_id(crud_db.Model):
    __tablename__='blog'
    id=crud_db.Column(crud_db.Integer,primary_key=True)
    blog=crud_db.Column(crud_db.String(1000),nullable=True)


@staticmethod
def get_all_blog():
    return blog_id.query.all()

@staticmethod
def get_for_id(id):
    return blog_id.query.get(id)