from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dwarzcqd:3_VIIhNE5FQQgULUNiBuEcqqBVI7c6zP@kesavan.db.elephantsql.com:5432/dwarzcqd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template('index.html')