from flask import Blueprint, render_template, request, redirect, session

from modules.admin.dashboard_home import get_player_roaster
from modules.admin.dashboard_tournament import get_tournament_details, post_tournament_details
from modules.admin.dashboard_events import get_event_details, assign_seeding

from modules.admin.dashboard_matches import get_matches_details

from modules.decoraters import admin_login_required

admin_app = Blueprint("admin", __name__)


@admin_app.route('/admin', methods=['GET', 'POST'])
@admin_login_required
def admin_dashboard():
    player_details = get_player_roaster()
    return render_template('admin/admin_dashboard.html', msg = player_details)


@admin_app.route('/admin/tournament', methods=['GET'])
@admin_login_required
def admin_form():
    tournament_details = get_tournament_details(request)
    return render_template('admin/admin_form.html', msg=tournament_details)


@admin_app.route('/admin/tournament_creation', methods=['POST'])
@admin_login_required
def admin_tournament_creation():
    if request.method == "POST":
        tournament_details = post_tournament_details(request)
        return render_template('admin/admin_form.html', msg=tournament_details)


@admin_app.route('/admin/events', methods=['GET'])
@admin_login_required
def admin_events():
    event_details = get_event_details()
    return render_template('admin/admin_events.html', msg=event_details)


@admin_app.route('/admin/enter_seed', methods=['POST'])
@admin_login_required
def enter_seed():
    if request.method == "POST":
        event_details = get_event_details()
        seed_updated_details = assign_seeding(request, event_details)
        return render_template('admin/admin_events.html', msg=seed_updated_details)


@admin_app.route('/admin/matches')
@admin_login_required
def admin_matches():
    print("Hello")
    match_details = get_matches_details()
    print(match_details)
    return render_template('admin/admin_matches.html', msg=match_details)
