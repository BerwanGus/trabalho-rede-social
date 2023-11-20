# Aqui vão estar os formulários do nosso site

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from tumbrl.models import User, Posts
from wtforms.widgets import TextArea


class FormLogin(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    btn = SubmitField('Login')


class FormCreateNewAccount(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    usarname = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 25)])
    checkPassword = PasswordField('Check Password', validators=[DataRequired(), Length(6, 25), EqualTo('password')])
    btn = SubmitField('Create Account')

    def validate_email(self, email):
        email_of_user = User.query.filter_by(email=email.data).first()
        if email_of_user:
            return ValidationError('~ email já existe ~')

class FormDeleteAccount(FlaskForm):
    btn = SubmitField('Delete Account')


class FormCreateNewPost(FlaskForm):
    text = StringField('Description', widget=TextArea(), validators=[DataRequired()])
    photo = FileField('Attach image', validators=[DataRequired()])
    btn = SubmitField('Publish')


class FormLikePost(FlaskForm):
    like_btn = SubmitField('Like')
    dislike_btn = SubmitField('Dislike')
