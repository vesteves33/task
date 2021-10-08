from flask import render_template, make_response
from flask_restful import Resource

class User(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('navbar.html'), 200, headers)