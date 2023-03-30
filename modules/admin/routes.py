from flask import Blueprint, render_template

admin_app = Blueprint("admin", __name__)


@admin_app.route('/admindashboard', methods=['GET', 'POST'])
def route_admin_dashboard():
    return render_template('admin/admindashboard.html')


@admin_app.route('/admindashboard_form')
def admindashboard_form():
    return render_template('admin/admindashboard_form.html')


@admin_app.route('/admindashboard_events')
def admindashboard_events():
    return render_template('admin/admindashboard_events.html')


@admin_app.route('/admindashboard_matches')
def admindashboard_matches():
    return render_template('admin/admindashboard_matches.html')
