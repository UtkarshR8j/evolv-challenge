from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields,Schema
import crud_blog

#crud_db=SQLAlchemy(app)


class blog_id(crud_db.Model):
    __tablename__='blog'
    id=crud_db.Column(crud_db.Integer,primary_key=True)
    blog=crud_db.Column(crud_db.String(1000),nullable=True)

def __init__(self):
    self.id=data.get('id')
    self.blog=data.get('blog')

def add(self):
    crud_db.session.add(self)
    crud_db.session.commit()

class blog_id_schema(Schema):
    id=fields.Int(required=True)
    blog=fields.Int(required=True)

crud_db.create_all()