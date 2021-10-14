from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.fields.core import IntegerField, SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, Length


class CreateAccount(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(message='Not a valid email adress.')])
    password = PasswordField('Password', validators=[DataRequired(), Length(6,16)])
    create = SubmitField('Create account')


class Login(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(message='Email not found, try again.')])
    password = PasswordField('Password', validators=[DataRequired(), Length(6,16)])
    lembrete = BooleanField('Keep me conected')
    login = SubmitField('Login')

class CreateProfile(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=40)])
    lastName = StringField('Last name', validators=[DataRequired(), Length(max=255)])
    cpf = IntegerField('Cpf', validators=[DataRequired(), Length(max=15)])
    profile = SubmitField('Create profile')

class CreateTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=40)])
    description = TextAreaField('Description')
    priority = SelectField('Priority', choices=[('none','None'), ('very-high','Very High'), ('high','High'), ('medium', 'Medium'), ('low', 'Low'), ('very-low', 'Very low')])
    task = SubmitField('Create task')