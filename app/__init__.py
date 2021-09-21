from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path


path = Path.cwd()
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}/app/db_task_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)

from app.routes import route