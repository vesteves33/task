from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class CreateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6,16)])
    create = SubmitField('Create')


class Login(FlaskForm):
    email_username = StringField('E-mail or Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6,16)])
    lembrete = BooleanField('Keep me conected')
    login = SubmitField('Login')