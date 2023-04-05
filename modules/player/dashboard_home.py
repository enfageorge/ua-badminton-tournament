from flask import session

from models.models import db
from models.tables.users import Users
from models.tables.player import Player


def get_player_details(user_id):
    db.session.expire_all()
    user = Users.query.get(user_id)
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
    return {**user_details, **player_details}


def edit_player_details(request, user_id):
    msg = ''
    current_user = Users.query.get(user_id)

    if request.form:
        if current_user.email != request.form['email']:
            # Update email in users table

            # Check if email already exists :
            email_exists = Users.query.filter_by(email=request.form['email']).first()
            if email_exists:
                msg += "ERROR : Could not update Email. Email already associated to another account."
            else:
                current_user.email = request.form['email']

    # Update players table
    player_obj = Player.query.get(session['user_id'])

    if request.form['phone_number']: player_obj.phone_number = request.form['phone_number']

    if request.form['dob']: player_obj.dob = request.form['dob']
    if request.form['club_name']: player_obj.club_name = request.form['club_name']

    db.session.commit()
    return True, msg
