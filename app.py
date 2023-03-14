from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlogin', methods =['GET', 'POST'])
def userlogin():  # need to be replace with real code talking to the database to do the authorization
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '1234':
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        elif username == 'jxu' and password == 'jf1234':
            msg = 'Logged in successfully !'
            return render_template('playerdashboard.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('userlogin.html', msg=msg)

@app.route('/usersignup')
def usersignup():
    return render_template('usersignup.html')

@app.route('/playerdash')
def playerdash():
    return render_template('playerdashboard.html')