from infer import app, model, response_obj as r
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
        func_queried = request.json['request']
    except KeyError as e:
        r.append(rtype='e', text='invalid json syntax, got '+e)
        func_queried = 'dummy'
    mc = model.Controller
    models = {
        "createNewElement": mc.create_new_element
    }
    try:
        call = models[func_queried]
    except KeyError as e:
        r.append(rtype='e', text='call to non-existing model: '+e)
        def call(*args): pass
    attr = request.json.get('attr', None)
    call(attr)
    return jsonify(r.prepare())
