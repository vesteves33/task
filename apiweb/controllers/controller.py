from flask.helpers import url_for
from flask_restful import Resource
from flask import render_template, make_response, request, flash, redirect, url_for
from apiweb.models.models import Account, User, save
from apiweb import bcrypt
from apiweb.formularios.forms import CreateAccount, Login


class Task(Resource):
    def get(self):
        return 'Hello World'

    def post(self):    
        pass

class User(Resource):
    def get(self):
        return make_response(render_template('index.html'))

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
                flash(f'Login feito com sucesso!')
                headers = {'Content-type': 'text/html'}
                return make_response(render_template('login.html', login=login), headers)

        
        
        