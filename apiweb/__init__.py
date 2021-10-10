from flask import Flask,Blueprint, render_template, make_response
from flask_restful import Api, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
api_bp = Blueprint('api',__name__)
api = Api(api_bp)
bcrypt = Bcrypt(app)
database = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage/db_taskmanager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#rotas da aplicação
from apiweb import route
app.register_blueprint(api_bp)






