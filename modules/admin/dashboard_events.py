from app import db
from models.tables.users import Users
from models.tables.players_event_seed import PlayersEventSeed
from models.tables.event import Event


def assign_seeding(request):
    ms_events_details = []
    ws_events_details = []
    md_events_details = []
    wd_events_details = []
    xd_events_details = []
    u19_events_details = []
    u17_events_details = []

    print(request.form)

    return {"ms_events_details": ms_events_details,
            "ws_events_details": ws_events_details,
            "md_events_details": md_events_details,
            "wd_events_details": wd_events_details,
            "xd_events_details": xd_events_details,
            "u19_events_details": u19_events_details,
            "u17_events_details": u17_events_details
            }


def get_event_details():
    db.session.expire_all()
    all_registrations = PlayersEventSeed.query.all()
    all_events = Event.query.all()
    ms_events_details = []
    ws_events_details = []
    md_events_details = []
    wd_events_details = []
    xd_events_details = []
    u19_events_details = []
    u17_events_details = []

    for event in all_events:
        if event.event_name == 'MS':
            ms_no = 1
            for reg_entry in all_registrations:
                if reg_entry.event_id == event.event_id:
                    user1_entry = Users.query.filter_by(id=reg_entry.player_1).first()
                    ms_events_details.append({
                        'id': ms_no,
                        'player1': user1_entry.first_name + ' ' + user1_entry.last_name,
                        'seed': reg_entry.seeding_score
                    })
                    ms_no += 1
        elif event.event_name == 'WS':
            ws_no = 1
            for reg_entry in all_registrations:
                if reg_entry.event_id == event.event_id:
                    user1_entry = Users.query.filter_by(id=reg_entry.player_1).first()
                    ws_events_details.append({
                        'id': ws_no,
                        'player1': user1_entry.first_name + ' ' + user1_entry.last_name,
                        'seed': reg_entry.seeding_score
                    })
                    ws_no += 1
        elif event.event_name == 'MD':
            md_no = 1
            for reg_entry in all_registrations:
                if reg_entry.event_id == event.event_id:
                    user1_entry = Users.query.filter_by(id=reg_entry.player_1).first()
                    user2_entry = Users.query.filter_by(id=reg_entry.player_2).first()
                    md_events_details.append({
                        'id': md_no,
                        'player1': user1_entry.first_name + ' ' + user1_entry.last_name,
                        'player2': user2_entry.first_name + ' ' + user2_entry.last_name,
                        'seed': reg_entry.seeding_score
                    })
                    md_no += 1
        elif event.event_name == 'WD':
            wd_no = 1
            for reg_entry in all_registrations:
                if reg_entry.event_id == event.event_id:
                    user1_entry = Users.query.filter_by(id=reg_entry.player_1).first()
                    user2_entry = Users.query.filter_by(id=reg_entry.player_2).first()
                    wd_events_details.append({
                        'id': wd_no,
                        'player1': user1_entry.first_name + ' ' + user1_entry.last_name,
                        'player2': user2_entry.first_name + ' ' + user2_entry.last_name,
                        'seed': reg_entry.seeding_score
                    })
                    wd_no += 1
        elif event.event_name == 'XD':
            xd_no = 1
            for reg_entry in all_registrations:
                if reg_entry.event_id == event.event_id:
                    user1_entry = Users.query.filter_by(id=reg_entry.player_1).first()
                    user2_entry = Users.query.filter_by(id=reg_entry.player_2).first()
                    xd_events_details.append({
                        'id': xd_no,
                        'player1': user1_entry.first_name + ' ' + user1_entry.last_name,
                        'player2': user2_entry.first_name + ' ' + user2_entry.last_name,
                        'seed': reg_entry.seeding_score
                    })
                    xd_no += 1
        elif event.event_name == 'U19':
            u19_no = 1
            for reg_entry in all_registrations:
                if reg_entry.event_id == event.event_id:
                    user1_entry = Users.query.filter_by(id=reg_entry.player_1).first()
                    u19_events_details.append({
                        'id': u19_no,
                        'player1': user1_entry.first_name + ' ' + user1_entry.last_name,
                        'seed': reg_entry.seeding_score
                    })
                    u19_no += 1
        elif event.event_name == 'U17':
            u17_no = 1
            for reg_entry in all_registrations:
                if reg_entry.event_id == event.event_id:
                    user1_entry = Users.query.filter_by(id=reg_entry.player_1).first()
                    u17_events_details.append({
                        'id': u17_no,
                        'player1': user1_entry.first_name + ' ' + user1_entry.last_name,
                        'seed': reg_entry.seeding_score
                    })
                    u17_no += 1

    return {"ms_events_details": ms_events_details,
            "ws_events_details": ws_events_details,
            "md_events_details": md_events_details,
            "wd_events_details": wd_events_details,
            "xd_events_details": xd_events_details,
            "u19_events_details": u19_events_details,
            "u17_events_details": u17_events_details
            }
