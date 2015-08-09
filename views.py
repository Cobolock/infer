from app import app
from app.response import Response
from app.controller import Controller
from flask import render_template, jsonify, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/r', methods=['POST'])
def handle_query():
    response = Response()
    controller = Controller(response)
    func_to_call = controller.get_func(request.json['request'])

    try:
        func_to_call(request.json['attr'])

    except ValueError:
        controller.log_error("Error: call to non-existent model: ")
        controller.log_error(request.json['attr'])
        response.append('e', 'Function was forgotten to be realized: ' +
                        func_to_call)

    print(response.answers)
    return jsonify(response.prepare())
