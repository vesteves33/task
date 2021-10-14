from apiweb.controllers.controller import Home, NewListTask, NewTask, NewUser, NewAccount,NewLogin
from apiweb import api

#Rotas da aplicação puxando diretamente do diretório de controllers
api.add_resource(Home, '/')
api.add_resource(NewListTask, '/tasks')
api.add_resource(NewTask, '/task/', '/task/<int:id>')
api.add_resource(NewUser, '/perfil')
api.add_resource(NewAccount, '/create')
api.add_resource(NewLogin, '/login')