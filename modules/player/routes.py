from flask import Blueprint, render_template

from modules.player.dashboard_home import get_player_profile_details

player_app = Blueprint("player", __name__)


@player_app.route('/dashboard', methods=['GET', 'POST'])
def player_dashboard():
    user_details = get_player_profile_details('username')
    return render_template('player/player_dashboard.html',msg =user_details)
