from itertools import groupby
from models.database import db
from models.models import Event, Users, PlayersEventSeed


def make_draws():
    """
    Function that is invoked when admin clicks 'make draw' that auto generates draws for everyone.
    """
    db.session.expire_all()
    player_event_seed_table = PlayersEventSeed.query.all()
    event_player_registrations = groupby(player_event_seed_table, lambda entry: entry.event_id)
    draws_info = [make_draw_for_one_event(event) for event in event_player_registrations]
    print(draws_info)
    return draws_info


def make_draw_for_one_event(event):
    # Get event information
    event_id, players = event
    event_details = Event.query.get(event_id)

    # Sort all players by seeding score
    sorted_players = sorted(players, key=lambda player: player.seeding_score)
    number_of_draws: int = int(len(sorted_players) / 2)
    draw_col0 = []

    for player_no in range(number_of_draws):
        player_set_one = sorted_players[player_no].player_1, sorted_players[player_no].player_2
        player_set_two = sorted_players[-1 - player_no].player_1, sorted_players[-1 - player_no].player_2

        if player_set_one[1] is not None:  # Doubles
            draw_col0.append([return_players_name(player_set_one[0]) + " , " + return_players_name(player_set_one[1]),
                              return_players_name(player_set_two[0]) + " , " + return_players_name(player_set_two[1])])
        else:  # Singles
            draw_col0.append([return_players_name(player_set_one[0]),
                              return_players_name(player_set_two[0])])

    # If there are an odd number of registrations, we pair a player with an empty placeholder player
    if len(sorted_players) % 2 != 0:  # There is an odd number of registrations
        middle_candidate = int(len(sorted_players) / 2) + 1
        player_set = sorted_players[middle_candidate].player_1, sorted_players[middle_candidate].player_2
        if player_set[1] is not None:  # Doubles
            draw_col0.append([return_players_name(player_set[0]) + " , " + return_players_name(player_set[1]),
                              " "])
        else:  # Singles
            draw_col0.append([return_players_name(player_set[0]), ""])

    return {
        'event_id': event_id,
        'event_name': event_details.event_name,
        'col_0': draw_col0
    }


def return_players_name(player_id):
    user_obj = Users.query.get(player_id)
    return " ".join([user_obj.first_name, user_obj.last_name])
