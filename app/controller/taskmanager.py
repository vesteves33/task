from app.models.task import Task
from ariadne import convert_kwargs_to_snake_case
from app import database

#CRUD - Class Task
def createTask(obj, info, title, description):
    try:
        task = Task(title=title, description=description)

        database.session.add(task)
        database.session.commit()
        payload = {
            "success":True,
            "task": task.returnTask()
        }
    except ValueError:
        payload = {
            "success":False,
            "errors": "Deu ruim na query rapa! Tente novamente" 
        }
    return payload


def getAllTasks(obj, info):
    try:
        tasks = [task.returnTask() for task in Task.query.all() ]
        payload = {
                "success":True,
                "tasks": tasks
            }
    except Exception as error:
        payload = {
                "success":False,
                "errors": [str(error)]
            }   
    return payload



def getTask(obj, info, id):
    try:
        task = Task.query.get(id)
        payload = {
            "success":True,
            "task": task.returnTask()
        }
    except AttributeError:
        payload = {
            "success":False,
            "errors": ["Task item matching {id} not found"]
        }
    return payload


def updateTask(obj, info, id, title, description):
    try:
        task = Task.query.get(id)

        if task:
            task.title = title
            task.description = description
        database.session.add(task)
        database.session.commit()
        payload = {
            "success": True,
            "task":task.returnTask()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Item matching id {id} not found"]
        }
    return payload

def deleteTask(obj, info, id):
    try:
        task = Task.query.get(id)
        
        if task:
            database.session.delete(task)
            database.session.commit()
        payload = {
            "success": True,
            "task": task.returnTask()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": "Task não encontrada"
        }
    return payload