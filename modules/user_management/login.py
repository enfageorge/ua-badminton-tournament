from flask import session
'''
This file contains functions that manage user signin and signup
'''


def user_signin(request):
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
        # account = cursor.fetchone()

        if username == 'admin' and password == 'pwd':
            account = {
                'id': 100,
                'username': 'admin',
            }
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']

            return True, 'Logged in', True
        elif username == 'user' and password == 'pwd':
            account = {
                'id': 400,
                'username': 'user',
            }
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return True, 'Logged in', False
        else:
            return False, 'Incorrect username / password', False
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
