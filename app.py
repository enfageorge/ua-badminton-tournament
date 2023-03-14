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

@app.route('/admindashboard')
def admindashboard():
    return render_template('admindashboard.html')

@app.route('/admindashboard_form')
def admindashboard_form():
    return render_template('admindashboard_form.html')

@app.route('/admindashboard_events')
def admindashboard_events():
    return render_template('admindashboard_events.html')

@app.route('/admindashboard_matches')
def admindashboard_matches():
    return render_template('admindashboard_matches.html')