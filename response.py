class Response:

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.answers = []

    def append(self, t, text, todo=None):
        if t not in ['a', 'w', 'e']:
            return 'Wrong Response type'
        d = {'a': 'answers',
             'w': 'warnings',
             'e': 'errors'}
        s = getattr(self, d[t])
        s.append({'text': text, 'todo': todo})

    def prepare(self):
        response = {}
        for l in ('answers', 'warnings', 'errors'):
            if getattr(self, l) != []:
                response[l] = getattr(self, l)

        return response
