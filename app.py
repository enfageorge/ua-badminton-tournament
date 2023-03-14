from flask import *
from modules.user_management.signin import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'PLACEHOLDER'  # TBA
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

app.secret_key = 'csc536'


@app.route('/')
def index():
    return render_template('home.html')


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


@app.route('/admin/dashboard', methods=['GET', 'POST'])
def route_admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def route_user_dashboard():
    return render_template('user_dashboard.html')


@app.route('/usersignup')
def usersignup():
    return render_template('usersignup.html')
