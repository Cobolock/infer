from functools import wraps
from infer import app, model, response_obj as r
from flask import render_template, jsonify, request, session, redirect, url_for, g


@app.route('/login')
def login():
    return 'not logged'


def authorize(f, access_level='manager', redirect_to='login'):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        u = session.get('user', None)
        if u is None:
            return redirect(url_for(redirect_to, next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@app.route('/index')
@authorize
def index():
    return render_template('index.html')


@app.route('/r', methods=['POST'])
@authorize
def handle_query():
    r.reset()

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
