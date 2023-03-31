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
    success_status, msg, is_admin = user_signin(request)
    if success_status:
        if is_admin:
            return redirect(url_for('admin.admin_dashboard'))
        else:
            return redirect(url_for('player.player_dashboard'))

    else:
        return render_template('user/login.html', msg=msg)
