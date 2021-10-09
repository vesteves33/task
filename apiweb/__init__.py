from flask import Flask,Blueprint, render_template, make_response
from flask_restful import Api, url_for
from pymongo import MongoClient
from flask_bcrypt import Bcrypt


app = Flask(__name__)
api_bp = Blueprint('api',__name__)
api = Api(api_bp)
bcrypt = Bcrypt(app)
conection = MongoClient("mongodb+srv://vitor_admin:bOyjcHBgdWfGxB3e@task-manager-cluster.vqrnk.mongodb.net/db_taskmanager?retryWrites=true&w=majority")
database = conection['db_taskmanager']

#rotas da aplicação
from apiweb import route
app.register_blueprint(api_bp)






