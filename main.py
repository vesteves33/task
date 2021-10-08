from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb+srv://vitor_admin:bOyjcHBgdWfGxB3e@task-manager-cluster.vqrnk.mongodb.net/task_manager?retryWrites=true&w=majority")

class Task(Resource):
    def get(self):
        
        return 'Muito obrigado xuxu, tu é a mais braba que nos temos! Bom descanso TMJ s2'

    

api.add_resource(Task, '/test/')






if __name__ == '__main__':
    app.run()