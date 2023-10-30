# Aqui vai as rotas e links
from instagram import app
from flask import render_template
from flask_login import login_required

from instagram.forms import FormLogin, FormCreateNewAccount  # Criar


# Adicionar methods
@app.route('/home', methods=['POST', 'GET'])
def homepage():
    formLogin = FormLogin()
    return render_template("home.html", form=formLogin)


@app.route('/new', methods=['POST', 'GET'])
def create_account():
    formNew = FormCreateNewAccount()
    return render_template("create_account.html", form=formNew)


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
