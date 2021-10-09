from apiweb.controllers.controller import Task, User, Account,Login
from apiweb import api

#Rotas da aplicação puxando diretamente do diretório de controllers
api.add_resource(Task, '/task/')
api.add_resource(User, '/')
api.add_resource(Account, '/create')
api.add_resource(Login, '/login')