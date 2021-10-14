from apiweb.controllers.controller import Task, User, NewAccount,NewLogin
from apiweb import api

#Rotas da aplicação puxando diretamente do diretório de controllers
api.add_resource(Task, '/task/')
api.add_resource(User, '/')
api.add_resource(NewAccount, '/create')
api.add_resource(NewLogin, '/login/<string:email>', '/login')