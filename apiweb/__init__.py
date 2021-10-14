from flask import Flask,Blueprint, render_template, make_response
from flask_restful import Api, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from pathlib import Path
import hashlib


app = Flask(__name__)
app.config['SECRET_KEY'] = hashlib.sha256().digest()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage/db_taskmanager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api_bp = Blueprint('api',__name__)
api = Api(api_bp)
bcrypt = Bcrypt(app)
database = SQLAlchemy(app)
#rotas da aplicação
from apiweb import route
app.register_blueprint(api_bp)
from apiweb.models.models import init_db

#Criando o banco de dados ao iniciar aplicação com todas as Models inseridas e configuradas
path = Path.cwd().joinpath('/apiweb/storage/').is_file()
if path == False:
    init_db(database)
#EXEMPLO DE HASH DA BCRYPT
#senha = 'xpto'
#hashSenha = bcrypt.generate_password_hash(senha) -> Criando o hash da informação
#verificaHash = bcrypt.check_password_hash(hashSenha, senha) -> Validando o valor do hash