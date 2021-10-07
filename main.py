from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def get(self):
        print('Hello World!')

    

api.add_resource(Task, '/task/')






if __name__ == '__main__':
    app.run(debug=True)