from flask import Blueprint, render_template

from modules.decoraters import admin_login_required

admin_app = Blueprint("admin", __name__)


@admin_app.route('/admin', methods=['GET', 'POST'])
@admin_login_required
def admin_dashboard():
    return render_template('admin/admin_dashboard.html')


@admin_app.route('/admin/tournament')
@admin_login_required
def admin_form():
    return render_template('admin/admin_form.html')


@admin_app.route('/admin/events')
@admin_login_required
def admin_events():
    return render_template('admin/admin_events.html')


@admin_app.route('/admin/matches')
@admin_login_required
def admin_matches():
    return render_template('admin/admin_matches.html')
