from flask import Blueprint, render_template, request

from modules.admin.dashboard_home import get_player_details
from modules.admin.dashboard_tournament import get_tournament_details
from modules.admin.dashboard_events import get_event_details
from modules.admin.dashboard_matches import get_matches_details

admin_app = Blueprint("admin", __name__)


@admin_app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    player_details = get_player_details('username')
    return render_template('admin/admin_dashboard.html', msg = player_details)


@admin_app.route('/admin/tournament', methods=['GET', 'POST'])
def admin_form():
    tournament_details = get_tournament_details('username', request)
    return render_template('admin/admin_form.html', msg = tournament_details)


@admin_app.route('/admin/events', methods=['GET', 'POST'])
def admin_events():
    event_details = get_event_details('username')
    return render_template('admin/admin_events.html',  msg = event_details)


@admin_app.route('/admin/matches')
def admin_matches():
    print("Hello");
    match_details = get_matches_details('username')
    print(match_details)
    return render_template('admin/admin_matches.html', msg = match_details)
