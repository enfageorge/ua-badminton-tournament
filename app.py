from flask import *
from modules.user_management.login import *
# from flask_sqlalchemy import SQLAlchemy

# Config

# app.config['SQLALCHEMY_DATABASE_URI'] = 'PLACEHOLDER'  # TBA
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
app = Flask(__name__)
app.secret_key = 'csc536'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admindashboard_form')
def admindashboard_form():
    return render_template('admindashboard_form.html')

@app.route('/admindashboard_events')
def admindashboard_events():
    return render_template('admindashboard_events.html')

@app.route('/admindashboard_matches')
def admindashboard_matches():
    return render_template('admindashboard_matches.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def route_user_signup():
    msg = user_signup(request)
    if msg == 'You have successfully registered !':
        return render_template('userlogin.html', msg=msg)
    else:
        return render_template('usersignup.html', msg=msg)


@app.route('/signin', methods=['GET', 'POST'])
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


@app.route('/admindashboard', methods=['GET', 'POST'])
def route_admin_dashboard():
    return render_template('admindashboard.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def route_user_dashboard():
    return render_template('playerdashboard.html')


# public view interface section
@app.route('/publicview_home', methods=['GET', 'POST'])
def route_public_interface():
    return render_template('publicview_home.html')

@app.route('/publicview_tournament')
def publicview_tournament_details():
    return render_template('publicview_tournament_details.html')

@app.route('/publicview_players')
def publicview_players():
    return render_template('publicview_players.html')

@app.route('/publicview_events')
def publicview_events():
    return render_template('publicview_events.html')

@app.route('/publicview_draws')
def publicview_draws():
    return render_template('publicview_draws.html')

@app.route('/publicview_matches')
def publicview_matches():
    return render_template('publicview_matches.html')