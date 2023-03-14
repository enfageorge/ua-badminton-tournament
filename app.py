from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'PLACEHOLDER'  # TBA
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

@app.route('/usersignup')
def usersignup():
    return render_template('usersignup.html')