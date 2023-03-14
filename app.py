from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'PLACEHOLDER'  # TBA
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

app.secret_key = 'csc536'
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/admin/signin',methods = ['GET', 'POST'])
def admin_signin():
        msg = ''
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            #cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
            #account = cursor.fetchone()

            account = {}

            if username == 'admin' and password == 'pwd':
                account = {
                    'id':102,
                    'username':'admin',
                }

            if account:
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                msg = 'Logged in successfully !'
                return render_template('admin_dashboard.html', msg=msg)
            else:
                msg = 'Incorrect username / password !'
        return render_template('admin_signin.html', msg=msg)


@app.route('/userlogin')
def user_login():
    return render_template('userlogin.html')

@app.route('/usersignup')
def usersignup():
    return render_template('usersignup.html')