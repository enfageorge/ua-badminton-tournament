from flask import session
from models.tables import Login

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

        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM accounts WHERE username = % s', (username,))
        # account = cursor.fetchone()

        # if account:
        if email == 'email0':
            msg = 'User exists, Try Logging in?'
        elif username == 'user0':
            msg = 'Username already exists. Choose a different username'
        else:
            # cursor.execute('INSERT INTO User VALUES (NULL, % s, % s, % s)', (username, password, email,))
            # mysql.connection.commit()
            msg = 'You have successfully registered !'
    return msg
