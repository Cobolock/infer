from infer import app
from flask import render_template, jsonify, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/r', methods=['POST'])
def handle_query():
    return 'olo'
