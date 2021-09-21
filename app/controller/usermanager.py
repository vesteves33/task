from app.models.user import User
from ariadne import convert_kwargs_to_snake_case
from app import database

#CRUD - Class User
def createUser(obj, info, name, email, cpf, password):
    try:
        user = User(name=name, email=email, cpf=cpf, password=password)

        database.session.add(user)
        database.session.commit()
        payload = {
            "success": True,
            "user": user.returnUser()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": ["Usuário não foi criado com sucesso, tente novamente"]
        }
    return payload
        

def updateUser(obj, info, id, name, email, password):
    try:
        user = User.query.get(id)

        if user:
            user.name = name
            user.email = email
            user.password = password
        database.session.add(user)
        database.session.commit()
        payload = {
            "success": True,
            "user": user.returnUser()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"The matching id {id} do not found any user"]
        }
    return payload

def deleteUser(obj, info, id):
    try:
        user = User.query.get(id)

        if user:
            database.session.delete(user)
            database.session.commit()
        payload = {
            "success": True,
            "user": user.returnUser()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"The id {id} do not found any user, try again!"]
        }
    return payload    

def getAllUsers(obj, info):
    try:
        users = [user.returnUsers() for user in User.query.all() ]
        payload = {
            "success":True,
            "users": users
        }

    except Exception as error:
        payload = {
            "success": False,
            "error": [f"{error}"]
        }
    return payload


def getUser(obj, info, id):
    try:
        user = User.query.get(id)

        payload = {
            "success": True,
            "user":user.returnUser()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"User id {id} not found"]
        }
    return payload

