from flask import Blueprint, render_template

web_app = Blueprint("web", __name__)


@web_app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('web/home.html')


@web_app.route('/tournament')
def tournament():
    return render_template('web/tournament.html')


@web_app.route('/players')
def players():
    return render_template('web/players.html')


@web_app.route('/events')
def events():
    return render_template('web/events.html')


@web_app.route('/draws')
def draws():
    return render_template('web/draws.html')


@web_app.route('/matches')
def matches():
    return render_template('web/matches.html')
