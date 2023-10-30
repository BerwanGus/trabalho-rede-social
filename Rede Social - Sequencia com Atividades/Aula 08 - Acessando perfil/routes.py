# Aqui vai as rotas e links
from instagram import app, bcrypt, database
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

from instagram.models import User  # Criar
from instagram.forms import FormLogin, FormCreateNewAccount, FormCreateNewPost  # Criar


@app.route('/profile/<user_id>', methods=['POST', 'GET'])  # AQUI
@login_required
def profile(user_id):
    if int(user_id) == int(current_user.id):
        # proprio perfil
        _formCreateNewPost = FormCreateNewPost()
        return render_template('profile.html', user=current_user, form=_formCreateNewPost)

    else:
        # vendo perfil de outro
        _user = User.query.get(int(user_id))
        return render_template('profile.html', user=_user)

