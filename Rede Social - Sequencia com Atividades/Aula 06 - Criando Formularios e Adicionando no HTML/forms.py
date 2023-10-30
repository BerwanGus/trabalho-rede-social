# Aqui vai ficar os formularios de login e de posts
# Criar tudo aqui :)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from instagram.models import User
from wtforms.widgets import TextArea


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    btn = SubmitField('Login')


class FormCreateNewAccount(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    usarname = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    checkPassword = PasswordField('Check Password', validators=[DataRequired(), Length(6, 20), EqualTo('password')])
    btn = SubmitField('Create Account')

    # ela tem o nome nesse padão para ser executada quando chamar-mos o 'validate on submit'.
    # Verifica se o email digitado já existe na tabela
    def validate_email(self, email):
        email_of_user = User.query.filter_by(email=email.data).first()
        if email_of_user:
            return ValidationError('~ email already exists ~')

