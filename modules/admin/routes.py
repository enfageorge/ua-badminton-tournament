from flask import Blueprint, render_template

admin_app = Blueprint("admin", __name__)


@admin_app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    return render_template('admin/admin_dashboard.html')


@admin_app.route('/admin/tournament')
def admin_form():
    return render_template('admin/admin_form.html')


@admin_app.route('/admin/events')
def admin_events():
    return render_template('admin/admin_events.html')


@admin_app.route('/admin/matches')
def admin_matches():
    return render_template('admin/admin_matches.html')
