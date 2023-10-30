# criar as rotas/links do site
import os
from werkzeug.utils import secure_filename
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user

from Completo.twitter.models import User, Posts
from Completo.twitter import app, database, bcrypt
from Completo.twitter.forms import FormLogin, FormCreateNewAccount, FormCreateNewPost


@app.route('/', methods=['POST', 'GET'])
def homepage():
    _formLogin = FormLogin()
    if _formLogin.validate_on_submit():
        userToLogIn = User.query.filter_by(email=_formLogin.email.data).first()
        if userToLogIn and bcrypt.check_password_hash(userToLogIn.password, _formLogin.password.data):
            login_user(userToLogIn)
            return redirect(url_for("profile", user_id=userToLogIn.id))

    return render_template('home.html', form=_formLogin)  # , form=formLogin)


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

    return render_template('criarconta.html', form=_formCreateAccount)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("homepage"))
