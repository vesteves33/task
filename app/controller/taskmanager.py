from app.models.Task import Task
from ariadne import convert_kwargs_to_snake_case

#class TaskManager:
def createTask():
          pass
def readTask(obj, info):
          try:
              tasks = [task.loadTask() for task in Task.query.all() ]
              print(tasks)
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

def listTask(obj, info, id):
    try:
        task = Task.query.get(id)
        payload = {
            "success":True,
            "task": task.loadTask()
        }
    except AttributeError:
        payload = {
            "success":False,
            "errors": ["Task item matching {id} not found"]
        }
    return payload


def updateTask():
          pass
    
def deleteTask():
          pass
