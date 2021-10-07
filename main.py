from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def get(self):
        print('Hello World!')

    def post(self):
        return 'Hello World2'

    def put(self):
        return "Hello world!"

    def delete(self):
        return 'hellO World!'


api.add_resource(Task, '/task/')






if __name__ == '__main__':
    app.run(debug=True)