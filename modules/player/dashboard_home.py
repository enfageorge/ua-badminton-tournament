from flask import session

from app import db
from models.tables.tournament import Tournament
from models.tables.event import Event
from models.tables.match import Match
from models.tables.login import Login
from models.tables.permission import Permission
from models.tables.player import Player
from models.tables.result import Result
from models.tables.user_permission import UserPermission
from models.tables.users import Users
from models.tables.players_event_seed import PlayersEventSeed
import json

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
    events_registered = PlayersEventSeed.query.all()
    event_list = []

    events = Event.query.all()
    event_DB = [event.event_name for event in events]
    event_list.append((event_DB))

    for event_regis in events_registered:
        event = Event.query.filter_by(event_id=event_regis.event_id).first()
        event_name = event.event_name
        player2 = None
        if event_regis.player_2 is not None:
            player2 = Users.query.filter_by(id=event_regis.player_2).first()
            player2 = player2.login_id
        event_list.append({event_name: player2})

    player_details = {
        'competing_gender': player.competing_gender,
        'phone_number': player.phone_number,
        'dob': player.dob,
        'club_name': player.club_name,
        'event': event_list
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

    events = PlayersEventSeed.query.all()

    events = Event.query.all()
    event_list = []
    for event in events:
        gender_allowed_list = [g.lower() for g in event.gender_allowed.split(',')]
        if player_obj.competing_gender in gender_allowed_list:
            event_list.append(event.event_name)

    # Get the event ids
    event_ids = [[event.event_id, event.event_name] for event in
                 Event.query.filter(Event.event_name.in_(event_list)).all()]

    # Loop over the events and update/create the entries in PlayersEventSeed
    for event_id in event_ids:
        # Check if an entry already exists
        event_seed = PlayersEventSeed.query.filter_by(player_1=player_obj.player_id, event_id=event_id[0]).first()

        # If an entry exists, update the fields
        if event_seed:
            player_2_id = request.form.get(event_id[1] + '_partner', None)
            if request.form[event_id[1]] not in ['WS', 'MS', 'U19', 'U17'] and player_2_id:
                player_2 = Users.query.filter_by(login_id=player_2_id).first()
                event_seed.player_2 = player_2.id
            else:
                event_seed.player_2 = None
        # If an entry does not exist, create a new instance of PlayersEventSeed and add it to the database
        else:
            if request.form[event_id[1]] not in ['WS', 'MS', 'U19', 'U17']:
                player_2_id = request.form.get(event_id[1] + '_partner', None)
                if player_2_id:
                    player_2 = Users.query.filter_by(login_id=player_2_id).first()
                new_event_seed = PlayersEventSeed(player_1=player_obj.player_id,
                                                  player_2=player_2_id.id,
                                                  seeding_score=0, event_id=event_id[0])
                db.session.add(new_event_seed)
            else:
                new_event_seed = PlayersEventSeed(player_1=player_obj.player_id, seeding_score=0, event_id=event_id[0])
                db.session.add(new_event_seed)
            db.session.commit()

    # Delete the entries that don't have a corresponding event in the event list
    for event_seed in PlayersEventSeed.query.filter_by(player_1=player_obj.player_id).all():
        event = Event.query.get(event_seed.event_id)
        if not event or event.event_name not in event_list:
            db.session.delete(event_seed)

    db.session.commit()
    return True, msg
