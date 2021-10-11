from apiweb import database
from datetime import datetime


#Aqui estarão as classes que serão representações de tabelas no BD

class Database:
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
    account = database.relationship('Account', backref='user', lazy=True)
    tasks = database.relationship('Task', backref='user', lazy=True)
    created_at = database.Column(database.DateTime, default=datetime.utcnow)
    updated_at = database.Column(database.DateTime, default=datetime.timestamp)

class Task(database.Model):
    __tablename__ = 'tb_task'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(40), nullable=False)
    description = database.Column(database.Text, nullable=True)
    priority = database.Column(database.String, default="Medium") #Valores do Campo no banco -> ['Very high', 'High', 'Medium', 'Low', 'Very low']
    status = database.Column(database.String, default="Backlog") #Valores do Campo no banco -> ['Backlog', 'In progress', 'Completed']
    created_at = database.Column(database.DateTime, default=datetime.utcnow) 
    updated_at = database.Column(database.DateTime, default=datetime.timestamp)
    user_id = database.Column(database.Integer, database.ForeignKey('tb_user.id'), nullable=False)

class Account(database.Model):
    __tablename__ = 'tb_account'
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(255), unique=True, nullable=False)
    username = database.Column(database.String(40), unique=True, nullable=False)
    password = database.Column(database.String(16), nullable=False)
    created_at = database.Column(database.DateTime,nullable=False, default=datetime.utcnow)
    updated_at = database.Column(database.DateTime, nullable=True, default=datetime.timestamp)
    #ForeignKey representando relação da conta com usuário
    user_id = database.Column(database.Integer, database.ForeignKey('tb_user.id'), nullable=False)

def init_db(self):
    self.create_all()