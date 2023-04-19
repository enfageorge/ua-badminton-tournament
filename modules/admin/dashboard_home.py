from models.models import db
from models.tables.users import Users
from models.tables.event_player import EventPlayer


def get_player_roaster():
    db.session.expire_all()
    users = Users.query.all()
    event_player_ids = EventPlayer.query.with_entities(EventPlayer.player_id).all()
    player_roaster = []
    s_no = 1
    for user in users:
        if user.player:
            # and user.player_id in event_player_ids
            # Uncomment this code once event player table has values
            player_roaster.append({
                'id': s_no,
                'username': user.login_id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            })
            s_no += 1
            
    return player_roaster
