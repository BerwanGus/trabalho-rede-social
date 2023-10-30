# Aqui vai as rotas e links
import os

from werkzeug.utils import secure_filename

from instagram import app, bcrypt, database
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

from instagram.forms import FormLogin, FormCreateNewAccount, FormCreateNewPost  # Criar
from instagram.models import User, Posts  # Criar


@app.route('/home', methods=['POST', 'GET'])
def homepage():
    _formLogin = FormLogin()
    if _formLogin.validate_on_submit():
        userToLogIn = User.query.filter_by(email=_formLogin.email.data).first()
        if userToLogIn and bcrypt.check_password_hash(userToLogIn.password, _formLogin.password.data):
            login_user(userToLogIn)
            return redirect(url_for("profile", user_id=userToLogIn.id))

    return render_template('home.html', form=_formLogin)


@app.route('/new', methods=['POST', 'GET'])
def create_account():
    _formCreateAccount = FormCreateNewAccount()

    if _formCreateAccount.validate_on_submit():
        password = _formCreateAccount.password.data
        password1 = bcrypt.generate_password_hash(_formCreateAccount.password.data)

        newUser = User(username=_formCreateAccount.usarname.data,
                       email=_formCreateAccount.email.data,
                       password=password1)

        database.session.add(newUser)
        database.session.commit()
        login_user(newUser, remember=True)
        return redirect(url_for("profile", user_id=newUser.id))
        # return render_template('criarconta.html', form=_formCreateAccount)

    return render_template('create_account.html', form=_formCreateAccount)


@app.route('/profile/<user_id>', methods=['POST', 'GET'])
@login_required
def profile(user_id):
    if int(user_id) == int(current_user.id):
        # proprio perfil
        _formCreateNewPost = FormCreateNewPost()
        if _formCreateNewPost.validate_on_submit():
            print('b')
            photo_file = _formCreateNewPost.photo.data
            photo_name = secure_filename(photo_file.filename)
            photo_path = f'{os.path.abspath(os.path.dirname(__file__))}/{app.config["UPLOAD_FOLDER"]}/{photo_name}'
            photo_file.save(photo_path)

            _post_text = _formCreateNewPost.text.data

            newPost = Posts(post_text=_post_text, post_img=photo_name, user_id=int(current_user.user_id))
            database.session.add(newPost)
            database.session.commit()
        return render_template('profile.html', user=current_user, form=_formCreateNewPost)

    else:
        # vendo perfil de outro
        _user = User.query.get(int(user_id))
        return render_template('profile.html', user=_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))


@app.route('/capaivara')
def capaivara():
    return render_template("capaivara.html")


@app.route('/teste')
def teste():
    return render_template("teste.html")

@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("homepage"))
