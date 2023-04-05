from datetime import datetime

from flask import redirect, url_for, session

from models.models import db
from models.tables import User
from models.tables.player import Player


def get_player_details(user_id):
    db.session.expire_all()
    user = User.query.get(user_id)
    user_details = {'username': user.login_id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'player_id': user.id,
                    }

    player = Player.query.get(user_id)
    player_details = {
        'competing_gender': player.competing_gender,
        'phone_number': player.phone_number,
        'dob': player.dob,
        'club_name': player.club_name
    }
    print({**user_details, **player_details})

    return {**user_details, **player_details}


def edit_player_details(request, user_id):
    msg = ''
    current_user = User.query.get(user_id)

    if request.form:
        if current_user.email != request.form['email']:
            # Update email in users table

            # Check if email already exists :
            email_exists = User.query.filter_by(email=request.form['email']).first()
            if email_exists:
                msg += "ERROR : Could not update Email. Email already associated to another account."
            else:
                current_user.email = request.form['email']

    # Update players table
    player_obj = Player.query.get(session['user_id'])

    if request.form['gender_optionsRadios']: player_obj.competing_gender = request.form['gender_optionsRadios']
    if request.form['phone_number']: player_obj.phone_number = request.form['phone_number']
    if request.form['dob']: player_obj.dob = datetime.utcnow() #request.form['dob']
    if request.form['club_name']: player_obj.club_name = request.form['club_name']

    db.session.commit()
    return True, msg
