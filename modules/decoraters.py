from functools import wraps

from flask import redirect, session, url_for, render_template


def user_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session['logged_in'] and session['user_id'] > 1:
            return f(*args, **kwargs)
        else:
            return render_template('user/login.html', msg='Login Required')

    return wrapper


def admin_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session['logged_in'] and session['user_id'] == 1:
            return f(*args, **kwargs)
        else:
            return render_template('user/login.html', msg='Admin Login Required')
    return wrapper
