from app import db
from models.tables.users import Users
from models.tables.players_event_seed import PlayersEventSeed


def get_event_details():
    db.session.expire_all()
    players_event_seed_ids = PlayersEventSeed.query.all()
    # eventids = Event.query.all()
    ms_events_details = []
    ws_events_details = []
    md_events_details = []
    wd_events_details = []
    xd_events_details = []
    u19_events_details = []
    u17_events_details = []

    ms_no = 1
    ws_no = 1
    md_no = 1
    wd_no = 1
    xd_no = 1
    for players_event_seed_id in players_event_seed_ids:
        if players_event_seed_id.eventid == 1:
            ms_events_details.append({
                'id': ms_no,
                'player1': players_event_seed_id.player_1,
                'seed': players_event_seed_id.seeding_score
            })
            ms_no += 1
        if players_event_seed_id.eventid == 2:
            ws_events_details.append({
                'id': ws_no,
                'player1': players_event_seed_id.player_1,
                'seed': players_event_seed_id.seeding_score
            })
            ws_no += 1
        if players_event_seed_id.eventid == 3:
            md_events_details.append({
                'id': md_no,
                'player1': players_event_seed_id.player_1,
                'player2': players_event_seed_id.player_2,
                'seed': players_event_seed_id.seeding_score
            })
            md_no += 1
        if players_event_seed_id.eventid == 4:
            wd_events_details.append({
                'id': wd_no,
                'player1': players_event_seed_id.player_1,
                'player2': players_event_seed_id.player_2,
                'seed': players_event_seed_id.seeding_score
            })
            wd_no += 1
        if players_event_seed_id.eventid == 5:
            xd_events_details.append({
                'id': xd_no,
                'player1': players_event_seed_id.player_1,
                'player2': players_event_seed_id.player_2,
                'seed': players_event_seed_id.seeding_score
            })
            xd_no += 1


    ms_events_details = [
        {
            'id': 1,
            'player1': 'Joe',
            'seed': '9'
        },
        {
            'id': 2,
            'player1': 'Michael',
            'seed': '10'
        }
    ]
    ws_events_details = [
        {
            'id': 1,
            'player1': 'Zoey',
            'seed': '12'
        },
        {
            'id': 2,
            'player1': 'Hanna',
            'seed': '10'
        }
    ]
    md_events_details = [
        {
            'id': 1,
            'player1': 'Neil',
            'player2': 'Jon',
            'seed': '15'
        },
        {
            'id': 2,
            'player1': 'Joey',
            'player2': 'Dan',
            'seed': '14'
        }
    ]
    wd_events_details = [
        {
            'id': 1,
            'player1': 'Jill',
            'player2': 'Rebecca',
            'seed': '18'
        },
        {
            'id': 2,
            'player1': 'Rina',
            'player2': 'Jennifer',
            'seed': '15'
        }
    ]
    xd_events_details = [
        {
            'id': 1,
            'player1': 'Kaden',
            'player2': 'Luna',
            'seed': '20'
        },
        {
            'id': 1,
            'player1': 'Lilly',
            'player2': 'Bruce',
            'seed': '22'
        }
    ]
    u19_events_details = [
        {
            'id': 1,
            'player1': 'Grace',
            'seed': '9'
        },
        {
            'id': 2,
            'player1': 'Malaya',
            'seed': '10'
        }
    ]
    u17_events_details = [
        {
            'id': 1,
            'player1': 'Mike',
            'seed': '10'
        }
    ]
    return {"ms_events_details": ms_events_details,
            "ws_events_details": ws_events_details,
            "md_events_details": md_events_details,
            "wd_events_details": wd_events_details,
            "xd_events_details": xd_events_details,
            "u19_events_details": u19_events_details,
            "u17_events_details": u17_events_details
            }
