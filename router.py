from infer import app, model, response_obj as r
from flask import render_template, jsonify, request, session, redirect, url_for


@app.route('/login')
def login():
    return 'not logged'


def authorize(f, access_level='manager', redirect_to='login'):
    try:
        currentUser = session.user
    except (KeyError, AttributeError):
        redirect(url_for(redirect_to))
    if currentUser.authorised:
        return f
    redirect(url_for(redirect_to))


@authorize
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@authorize
@app.route('/r', methods=['POST'])
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
