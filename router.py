from functools import wraps
from infer import app, model, user, response_obj as r
from flask import render_template, jsonify, request, session, redirect, url_for, g


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            u = session['user']
        except KeyError:
            u = session['user'] = {}
            u['name'] = request.form['userName']
            u['role'] = user.User.names.get(u['name'], 1)
        if 'next' in request.args:
            next_hop = request.args['next']
            print(next_hop)
            if next_hop.startswith('/'):
                next_hop = next_hop[1:]
            next_hop = 'index' if next_hop == '' else next_hop
        else:
            next_hop = 'index'
        g.users = g.get('users', [])
        if u['name'] not in g.users:
            g.users.append(u['name'])
        return redirect(url_for(next_hop))
    return render_template('login.html')


def authorize(f, access_level='manager', redirect_to='login'):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        u = session.get('user', None)
        if u is None:
            return redirect(url_for(redirect_to, next=request.path))
        if u is not None and u['role'] < user.User.levels[access_level]:
            return redirect(url_for(request.path, message='access denied'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@app.route('/index')
@authorize
def index():
    users = g.get('users', False)
    return render_template('index.html', users=users)


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
