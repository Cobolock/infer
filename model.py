from infer import session, response_obj as r


class Controller:

    def __init__(self):
        pass

    def create_new_element(attr):
        if 'names' not in session:
            session['names'] = []
        session['names'].append(attr['name'])
        r.append(rtype='a', text=','.join(session['names']))
