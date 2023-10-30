from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  # Importar
from flask_bcrypt import Bcrypt  # Importar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = 'c36d4f415b226400c2995bb86f99c3d6'
app.config['UPLOAD_FOLDER'] = 'ststic/fotos_dos_posts'  # Adicionar

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from instagram import routes
