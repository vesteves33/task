from sqlalchemy.orm import backref
from apiweb import database
from datetime import datetime


#Aqui estarão as classes que serão representações de tabelas no BD
def init_db(self):
    self.create_all()

def save(self):
    database.session.add(self)
    database.session.commit()

def listAll(self):
    database.query.all()

def listOne(self):
    database.query.filter_by(self).first()

def delete(self):
    database.session.delete(self)
    database.session.commit()

class User(database.Model):
    __tablename__ = 'tb_user'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(40), nullable=True)
    lastName = database.Column(database.String(255), nullable=True)
    cpf = database.Column(database.Integer, unique=True, nullable=True)
    created_at = database.Column(database.DateTime, default=datetime.utcnow)
    account_id = database.Column(database.Integer, database.ForeignKey('tb_account.id'), nullable=False)

class Task(database.Model):
    __tablename__ = 'tb_task'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(40), nullable=False)
    description = database.Column(database.Text, nullable=True)
    priority = database.Column(database.String, default="Medium") #Valores do Campo no banco -> ['Very high', 'High', 'Medium', 'Low', 'Very low']
    status = database.Column(database.String, default="Backlog") #Valores do Campo no banco -> ['Backlog', 'In progress', 'Completed']
    created_at = database.Column(database.DateTime, default=datetime.utcnow) 
    account_id = database.Column(database.Integer, database.ForeignKey('tb_account.id'), nullable=False)

class Account(database.Model):
    __tablename__ = 'tb_account'
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(255), unique=True, nullable=False)
    password = database.Column(database.String(16), nullable=False)
    created_at = database.Column(database.DateTime,nullable=False, default=datetime.utcnow)
    #ForeignKey representando relação da conta com usuário
    user = database.relationship('User', backref='account', lazy=True)
    tasks = database.relationship('Task', backref='account', lazy=True)
