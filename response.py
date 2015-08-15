class Response:

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.answers = []

    def append(self, *args, rtype='e', text='default text', todo=None):
        if rtype not in ['a', 'w', 'e']:
            self.append(rtype='e', text='wrong response type')
        d = {'a': 'answers',
             'w': 'warnings',
             'e': 'errors'}
        l = getattr(self, d[rtype])
        a = {'text': text, 'todo': todo} if todo is not None else {
            'text': text}
        l.append(a)

    def prepare(self):
        response = {}
        for l in ('answers', 'warnings', 'errors'):
            if getattr(self, l) != []:
                response[l] = getattr(self, l)

        return response
