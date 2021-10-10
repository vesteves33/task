from apiweb import database
from datetime import datetime


#Aqui estarão as classes que serão representações de tabelas no BD

class User(database.Model):
    __tablename__ = 'tb_user'
    id = database.Column(database.Integer(), primary_key=True)
    name = database.Column()
    lastName = database.Column()
    cpf = database.Column()
    email = database.Column()
    username = database.Column()
    password = database.Column()
    created_at = database.Column(database.DateTime(default=datetime.utcnow()))
    updated_at = database.Column(database.DateTime(default=datetime.timestamp()))

class Task(database.Model):
    __tablename__ = 'tb_task'
    id = database.Column(database.Integer(), primary_key=True)
    title = database.Column()
    description = database.Column()
    priority = database.Column(['Very high', 'High', 'Medium', 'Low', 'Very low'])
    status = database.Column(['Backlog', 'In progress', 'Completed'])
    created_at = database.Column() 
    updated_at = database.Column()

