from flask import session
from models.tables import Login, User

'''
This file contains functions that manage player signin and signup
'''


def user_signin(request):
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Get user from db
        login_user = Login.query.get(username)

        if login_user:
            correct_password = login_user.password

            if username == 'admin' and password == correct_password:
                session['loggedin'] = True
                session['username'] = login_user.login_id
                return True, 'Logged in', True

            elif password == correct_password:
                account = {
                    'id': 400,
                    'username': 'player',
                }
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                return True, 'Logged in', False
            elif password != correct_password:
                return False, 'Incorrect username / password', False
        else:
            return False, 'No account found,check username or please sign up', False
    return False, '', False


def user_signup(request):
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and \
            'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if user already exists in db:
        login_user = Login.query.get(username)
        user_exists = User.query.filter_by(email=email).first()
        if login_user:
            if user_exists:
                if user_exists.email == email:  # username and email found in db
                    msg = 'User exists, Try Logging in?'
            else:  # Someone has that username already
                msg = 'Sorry, that username is taken. Try another?'
        elif user_exists:  # Username is incorrect, but the email exists in db
            msg = 'User exists, Try Logging in?'
        else:  # todo: Insert a new user
            msg = 'You have successfully registered !'
    return msg
