# Aqui vão as rotas e os links
from tumbrl import app
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user
from tumbrl.models import load_user
from tumbrl.forms import FormLogin, FormCreateNewAccount
from tumbrl import bcrypt
from models import User
from tumbrl import database


# @app.route('/home')
@app.route('/', methods=['POST', 'GET'])
def homepage():
    _formLogin = FormLogin()
    return render_template('home.html', textinho='TOP', form=_formLogin)


@app.route('/new', methods=['POST', 'GET'])
def createAccount():
    _formCreateNewAccount = FormCreateNewAccount()

    if _formCreateNewAccount.validate_on_submit():
        password = _formCreateNewAccount.password.data
        password_cr = bcrypt.generate_password_hash(password)
        # print(password)
        # print(password_cr)

        newUser = User(
            username=_formCreateNewAccount.usarname.data,
            email=_formCreateNewAccount.email.data,
            password=password
        )

        database.session.add(newUser)
        database.session.commit()

        # Desafio
        # Fazer Login e Mandar para a pagina de perfil dele

        login_user(newUser, remember=True)
        return redirect(url_for('profile.html', user_id=newUser.id))

    return render_template('new.html', form=_formCreateNewAccount)


@app.route('/perry')
def perry():
    return render_template('perry.html')


@app.route('/teste')
def teste():
    return render_template('teste.html')


@app.route('/profile/<user_id>')  # /<batata>')
@login_required
def profile(user_id):  # , batata):
    return render_template('profile.html', user=user_id)  # , mesa=batata)
