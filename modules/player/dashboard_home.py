from flask import session

from models.models import db
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
    events = Event.query.all()
    event_name = []

    for event in events:
        gender_allowed_list = [g.lower() for g in event.gender_allowed.split(',')]
        if player.competing_gender in gender_allowed_list:
            event_name.append(event.event_name)

    names_string = ", ".join(event_name)
    player_details = {
        'competing_gender': player.competing_gender,
        'phone_number': player.phone_number,
        'dob': player.dob,
        'club_name': player.club_name,
        'event': names_string
    }

    return {**user_details, **player_details}


def edit_player_details(request, user_id):
    msg = ''

    print("Request: ", request)
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
    print(events)

    events = Event.query.all()
    event_list = []
    for event in events:
        gender_allowed_list = [g.lower() for g in event.gender_allowed.split(',')]
        if player_obj.competing_gender in gender_allowed_list:
            event_list.append(event.event_name)

    # events_list_request = json.loads(request.form['event'])
    # print(request.form['event'])
    # events_request = [key for event_dict in events_list_request for key in event_dict.keys()]

    # for event in events_list:
    #     if event in event_name and event in events_request:
    #         event_dict = next((d for d in events_list_request if d.get(event)), None)
    #         event_entry = Event.query.filter_by(event_name=event).first()
    #         if event_dict:
    #             if event_entry.gender_allowed != event_dict[event]['gender_allowed']:
    #                 event_entry.gender_allowed = event_dict[event]['gender_allowed']
    #             if event_entry.max_participants_allowed != event_dict[event]['max_participants_allowed']:
    #                 event_entry.max_participants_allowed = event_dict[event]['max_participants_allowed']
    #             db.session.commit()
    #     elif event in event_name and event not in events_request:
    #         event_entry = Event.query.filter_by(event_name=event).first()
    #         db.session.delete(event_entry)
    #         db.session.commit()
    #     elif event not in event_name and event in events_request:
    #         event_dict = next((d for d in events_list_request if d.get(event)), None)
    #         if event_dict:
    #             new_event = Event(event, event_dict[event]['gender_allowed'],
    #                               event_dict[event]['max_participants_allowed'])
    #             db.session.add(new_event)
    #             db.session.commit()

    db.session.commit()
    return True, msg
