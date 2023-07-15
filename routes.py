from website import app
from flask import render_template, redirect, url_for


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/landing')
def dashboard():
    return render_template('dashboard.html')