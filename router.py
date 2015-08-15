from infer import app
from flask import render_template, jsonify, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return 'not logged'


@app.route('/r', methods=['POST'])
def handle_query():
    try:
        func_query = request.json['request']
    except Exception as e:
        print(type(e))
    return ''
