from flask import Flask, Blueprint, render_template, make_response
from flask_restful import Api, Resource, url_for
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
bcrypt = Bcrypt(app)
#client = MongoClient("mongodb+srv://vitor_admin:bOyjcHBgdWfGxB3e@task-manager-cluster.vqrnk.mongodb.net/task_manager?retryWrites=true&w=majority")
#database = client.test

class Task(Resource):
    def get(self):
        
        return 'Hello World'

api.add_resource(Task, '/test/')
app.register_blueprint(api_bp)

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('navbar.html'), 200, headers)
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run()


