from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

@app.route('/usersignup')
def usersignup():
    return render_template('usersignup.html')

@app.route('/playerdash')
def playerdash():
    return render_template('playerdashboard.html')