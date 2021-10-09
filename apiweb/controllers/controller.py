from flask_restful import Resource
from flask import render_template, make_response, request
from werkzeug.utils import redirect
from apiweb.models.user import User
from apiweb import database
import json

class Task(Resource):
    def get(self):
        return 'Hello World'

    def post(self):    
        pass

class User(Resource):
    def get(self):
        return make_response(render_template('index.html'))

class Account(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('signup.html'), 200, headers)

    def post(self):
        response = request.form.to_dict()
        user = database.User.insert_one(response)
        
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('signup.html'),headers)

class Login(Resource):
    def get(self):
        headers = {'Content-type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)
    
    def post(self):
        response = request.form.to_dict()
        return response
        

        
        
        