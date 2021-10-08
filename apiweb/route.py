from apiweb.controllers.taskController import Task
from apiweb.controllers.userController import User
from apiweb import api

#Rotas da aplicação puxando diretamente do diretório de controllers
api.add_resource(Task, '/task/')
api.add_resource(User, '/')