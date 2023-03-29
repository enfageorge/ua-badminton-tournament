from flask import Blueprint,request,render_template,redirect,url_for
from modules.user_management.login import *

user_management_app = Blueprint("user_management",__name__)


@user_management_app.route('/signup', methods=['GET', 'POST'])
def route_user_signup():
    msg = user_signup(request)
    if msg == 'You have successfully registered !':
        return render_template('userlogin.html', msg=msg)
    else:
        return render_template('usersignup.html', msg=msg)


@user_management_app.route('/signin', methods=['GET', 'POST'])
def route_user_signin():
    success_status: bool
    success_status, msg, is_admin = user_signin(request)
    if success_status:
        if is_admin:
            return redirect(url_for('route_admin_dashboard'))
        else:
            return redirect(url_for('route_user_dashboard'))

    else:
        return render_template('userlogin.html', msg=msg)
