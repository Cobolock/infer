class User:

    def get(self, seed, default):
        return getattr(self, seed, default)

    levels = {
        'guest': 1,
        'manager': 2,
        'admin': 3
    }

    names = {
        'admin': 3,
        'lol': 2
    }
