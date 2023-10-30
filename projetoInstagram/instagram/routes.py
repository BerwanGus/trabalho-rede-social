# Aqui vai as rotas e links
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user
from instagram.models import load_user, User
from instagram import app, database
from instagram.forms import FormLogin, FormCreateNewAccount
from instagram import bcrypt


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def homepage():
    formLogin = FormLogin()

    if formLogin.validate_on_submit():
        userToLogin = User.query.filter_by(email=formLogin.email.data).first()
        if userToLogin and bcrypt.check_password_hash(userToLogin.password, formLogin.password.data):
            load_user(userToLogin.id)
            return redirect(url_for('profile', user_id=userToLogin.id))


    return render_template("home.html", teto='HOME', form=formLogin)


@app.route('/profile/<user_id>')
@login_required
def profile(user_id):
    return render_template("profile.html", user=user_id)


@app.route('/capaivara')
def capaivara():
    return render_template("capaivara.html")


@app.route('/teste')
def teste():
    return render_template("teste.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/new', methods=['POST', 'GET'])
def create_account():
    formCreateAccount = FormCreateNewAccount()

    if formCreateAccount.validate_on_submit():
        password = formCreateAccount.password.data
        password_cr = bcrypt.generate_password_hash(password)
        # print(password)
        # print(password1)

        newUser = User(username=formCreateAccount.username.data,
                       email=formCreateAccount.email.data,
                       password=password_cr)

        database.session.add(newUser)
        database.session.commit()
        login_user(newUser, remember=True)
        return redirect(url_for('profile', user_id=newUser.id))

    return render_template("new.html", form=formCreateAccount)
