from models.models import db
from models.tables.users import Users
from models.tables.event_player import EventPlayer
# from models.tables.players_event_seed import PlayersEventSeed
from models.tables.event import Event

def get_event_details(username):
    db.session.expire_all()
    players_event_seed_ids = PlayersEventSeed.query.all()
    eventids = Event.query.all()
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


    return {"ms_events_details": ms_events_details,
            "ws_events_details": ws_events_details,
            "md_events_details": md_events_details,
            "wd_events_details": wd_events_details,
            "xd_events_details": xd_events_details,
            "u19_events_details": u19_events_details,
            "u17_events_details": u17_events_details
            }
