from enum import unique
from app import database
from datetime import datetime

class User(database.Model):
    __tablename__ = "tb_user"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120),unique=True, nullable=False)
    cpf = database.Column(database.Integer, lenght=11, unique=True)
    password = database.Column(database.String(20), nullable=False)
    created_at = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())

    def returnUser(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cpf": self.cpf,
            "password": self.password,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }