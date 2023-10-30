# Aqui vai as rotas e links
from instagram import app, bcrypt, database
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

from instagram.forms import FormLogin, FormCreateNewAccount, FormCreateNewPost
from instagram.models import User, Posts

import os  # Importar
from werkzeug.utils import secure_filename # Importar


@app.route('/profile/<user_id>', methods=['POST', 'GET'])
@login_required
def profile(user_id):
    if int(user_id) == int(current_user.id):
        # proprio perfil
        _formCreateNewPost = FormCreateNewPost()

        if _formCreateNewPost.validate_on_submit():
            photo_file = _formCreateNewPost.photo.data
            photo_name = secure_filename(photo_file.filename)  # Nome seguro
            photo_path = f'{os.path.abspath(os.path.dirname(__file__))}/{app.config["UPLOAD_FOLDER"]}/{photo_name}'
            photo_file.save(photo_path)  # Da para uar os.path.join (mas acho feio)

            _post_text = _formCreateNewPost.text.data

            newPost = Posts(post_text=_post_text, post_img=photo_name, user_id=int(current_user.user_id))
            database.session.add(newPost)
            database.session.commit()
        return render_template('profile.html', user=current_user, form=_formCreateNewPost)

    else:
        # vendo perfil de outro
        _user = User.query.get(int(user_id))
        return render_template('profile.html', user=_user, form=None)
