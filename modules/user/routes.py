from flask import Blueprint, request, render_template, redirect, url_for
from modules.user.login import *

user_app = Blueprint("user", __name__)


@user_app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = user_signup(request)
    if msg == 'You have successfully registered !':
        return render_template('user/login.html', msg=msg)
    else:
        return render_template('user/signup.html', msg=msg)


@user_app.route('/signin', methods=['GET', 'POST'])
def signin():
    success_status: bool
    success_status, msg = user_signin(request)
    if success_status:
        print(session['user_id'])
        if session['user_id'] == 1:
            return redirect(url_for('admin.admin_dashboard'))
        else:
            return redirect(url_for('player.player_dashboard'))
    else:
        return render_template('user/login.html', msg=msg)
