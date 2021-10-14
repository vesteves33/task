from flask import Flask, render_template, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_restful import Api, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from pathlib import Path
import hashlib


app = Flask(__name__)
app.config['SECRET_KEY'] = hashlib.sha256().digest()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage/db_taskmanager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = hashlib.sha256().digest()

api = Api(app)
bcrypt = Bcrypt(app)
database = SQLAlchemy(app)
jwt = JWTManager(app)
#rotas da aplicação
from apiweb import route
from apiweb.models.models import init_db

#Criando o banco de dados ao iniciar aplicação com todas as Models inseridas e configuradas
path = Path.cwd().joinpath('/apiweb/storage/').is_file()
if path == False:
    init_db(database)
