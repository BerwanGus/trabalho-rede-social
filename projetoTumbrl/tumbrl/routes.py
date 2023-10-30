# Aqui vão as rotas e os links
from tumbrl import app
from flask import render_template, url_for
from flask_login import login_required
from tumbrl.models import load_user

# @app.route('/home')
@app.route('/')
def homepage():
    return render_template('home.html', textinho='TOP')


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

