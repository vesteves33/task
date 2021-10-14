from flask.helpers import url_for
from flask_restful import Resource
from flask import render_template, make_response, request, flash, redirect, url_for
from apiweb.models.models import Account, Task, User, save
from apiweb import bcrypt
from apiweb.formularios.forms import CreateAccount, Login, CreateProfile, CreateTask



class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), headers)


class NewListTask(Resource):
    def get(self):
        tasks = Task.query.all()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('tasks.html', tasks=tasks), headers)
            

            
        
        



class NewTask(Resource):
    def get(self):
        createTask = CreateTask()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('task.html', createTask=createTask),200, headers)

    def post(self):    
        createTask = CreateTask()
        
        if createTask.validate_on_submit() and 'task' in request.form:
            task = Task(title=createTask.title.data, description=createTask.description.data, priority=createTask.priority.data, account_id=1)
            if task.priority == 'none':
                task.priority = 'medium'
                
            save(task)
            
            
            headers = {'Content-Type': 'text/html'}
            flash(f'Task criada com sucesso:{task.id}', 'alert-sucess')
            return make_response(render_template('task.html', createTask=createTask), headers)

    def put(self, id):
        pass

    def delete(self, id):
        pass    


class NewUser(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass    



class NewAccount(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        createAccount = CreateAccount()
        return make_response(render_template('signup.html', createAccount=createAccount), 200, headers)

    def post(self):
        createAccount = CreateAccount()
        
        if createAccount.validate_on_submit() and 'create' in request.form:
            password_hash = bcrypt.generate_password_hash(createAccount.password.data)

            account = Account(email=createAccount.email.data, password=password_hash)
            #função save encapsula os métodos do Database
            save(account)

            headers = {'Content-Type': 'text/html'}

            flash(f'Conta criada com sucesso para o Email: {createAccount.email.data}', 'alert-success')
            return make_response(render_template('signup.html', createAccount=createAccount), headers)

        

class NewLogin(Resource):
    def get(self):
        login = Login()
        headers = {'Content-type': 'text/html'}
        return make_response(render_template('login.html',login=login), 200, headers)
    
    def post(self):
        login = Login()

        if login.validate_on_submit() and 'login' in request.form:
            account = Account.query.filter_by(email=login.email.data).first()

            if account and bcrypt.check_password_hash(account.password, login.password.data):
                flash(f'Login feito com sucesso!', 'alert-success')
                headers = {'Content-type': 'text/html'}
                return make_response(render_template('login.html', login=login), headers)

        
        
        