# Aqui vai as rotas e links
from flask import render_template
from instagram import app


@app.route('/home')
def homepage():
    var = 'HOME'
    return render_template("home.html", teto=var)


@app.route('/profile/<user_id>')
def profile(user_id):
    return render_template("profile.html", user=user_id)


@app.route('/capaivara')
def capaivara():
    return render_template("capaivara.html")


@app.route('/teste')
def teste():
    return render_template("teste.html")

