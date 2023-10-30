# Aqui vai as rotas e links
from instagram import app, bcrypt, database
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

from instagram.forms import FormLogin, FormCreateNewAccount, FormCreateNewPost
from instagram.models import User, Posts

import os
from werkzeug.utils import secure_filename


@app.route('/feed', methods=['POST', 'GET'])
@login_required  # Se quiser
def feed():
    # allPosts = Posts.query.order_by(Posts.creation_date).all()  # ordem para mostrar
    allPosts = Posts.query.order_by(Posts.creation_date.desc()).all()
    return render_template("feed.html", all_posts=allPosts, User=User)
