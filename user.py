class User:

    def get(seed, default):
        return getattr(User, seed, default)

    levels = {
        'guest': 1,
        'manager': 2,
        'admin': 3
    }

    names = {
        'admin': 3,
        'lol': 2
    }
