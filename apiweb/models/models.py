from apiweb import database
from datetime import datetime


#Aqui estarão as classes que serão representações de tabelas no BD

class User(database.Model):
    __tablename__ = 'tb_user'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(40), nullable=True)
    lastName = database.Column(database.String(255), nullable=True)
    cpf = database.Column(database.Integer, unique=True, nullable=True)
    account = database.relationship('Account', backref='user', lazy=True)
    tasks = database.relationship('Task', backref='user', lazy=True)
    created_at = database.Column(database.DateTime, default=datetime.utcnow)
    updated_at = database.Column(database.DateTime, default=datetime.timestamp)

class Task(database.Model):
    __tablename__ = 'tb_task'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(40), nullable=False)
    description = database.Column(database.Text(40), nullable=True)
    priority = database.Column(database.String,  ['Very high', 'High', 'Medium', 'Low', 'Very low'])
    status = database.Column(database.String, ['Backlog', 'In progress', 'Completed'])
    created_at = database.Column(database.DateTime, default=datetime.utcnow) 
    updated_at = database.Column(database.DateTime, default=datetime.timestamp)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)

class Account(database.Model):
    __tablename__ = 'tb_account'
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(255), unique=True, nullable=False)
    username = database.Column(database.String(40), unique=True, nullable=False)
    password = database.Column(database.String(16), nullable=False)
    created_at = database.Column(database.DateTime,nullable=False, default=datetime.utcnow)
    updated_at = database.Column(database.DateTime, nullable=True, default=datetime.timestamp)
    #ForeignKey representando relação da conta com usuário
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
