from flask import Flask
from flask import render_template 
from app import app


@app.route('/')
def home():
    return render_template('signup.html')