from functools import wraps
from flask import redirect, url_for, request, g


def login_required(f):
    '''Giriş yapılması gerekli alanlar için kontrol yapan decarator.'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function