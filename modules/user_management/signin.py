from flask import session


def user_signin(request):
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
        # account = cursor.fetchone()

        # Temp password
        account = {}

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
            return False, 'Incorrect username / password',False
    return False, '', False
