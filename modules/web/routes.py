from flask import Blueprint, request, render_template, redirect, url_for

web_app = Blueprint("web", __name__)


@web_app.route('/publicview_home', methods=['GET', 'POST'])
def route_public_interface():
    return render_template('publicview_home.html')


@web_app.route('/publicview_tournament')
def publicview_tournament_details():
    return render_template('publicview_tournament_details.html')


@web_app.route('/publicview_players')
def publicview_players():
    return render_template('publicview_players.html')


@web_app.route('/publicview_events')
def publicview_events():
    return render_template('publicview_events.html')


@web_app.route('/publicview_draws')
def publicview_draws():
    return render_template('publicview_draws.html')


@web_app.route('/publicview_matches')
def publicview_matches():
    return render_template('publicview_matches.html')
