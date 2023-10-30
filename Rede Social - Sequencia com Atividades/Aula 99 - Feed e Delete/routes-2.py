# criar as rotas/links do site
import os
from flask_login import login_required, login_user, logout_user, current_user
from flask import render_template, url_for, redirect
from werkzeug.utils import secure_filename

from Completo.twitter.models import User, Posts
from Completo.twitter import app, database, bcrypt
from Completo.twitter.forms import FormLogin, FormCreateNewAccount, FormCreateNewPost


@app.route('/feed', methods=['POST', 'GET'])
def feed():
    allPosts = Posts.query.order_by(Posts.creation_date.desc()).all()
    return render_template("feed.html", posts=allPosts, User=User)


@app.route('/delete/<post_id>', methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    print('AA:', post_id)
    post = Posts.query.filter_by(post_id=post_id).first()
    print('BB: ', post)
    database.session.delete(post)
    database.session.commit()
    return redirect(url_for("profile", user_id=current_user.user_id))
