# Vai as classes / estrura do banco de dados
from instagram import database
from datetime import datetime


class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    posts = database.relationship("Posts", backref='user', lazy=True)


class Posts(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    post_text = database.Column(database.String, default='')
    post_img = database.Column(database.String, default='default.png')
    creation_date = database.Column(database.String, nullable=False, default=datetime.utcnow())
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
