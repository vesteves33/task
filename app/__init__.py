from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home(name='Vitor'):
    return render_template('index.html', name=name)