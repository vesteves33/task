from flask import Flask
from flask import render_template, url_for
from app import app


@app.route('/')
def home():
    return render_template('header.html')