from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  # Importar
from flask_bcrypt import Bcrypt  # Importar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = 'c36d4f415b226400c2995bb86f99c3d6'  # Adicionar

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)  # Criar
login_manager = LoginManager(app)  # Criar
login_manager.login_view = 'homepage'  # Criar

from instagram import routes
