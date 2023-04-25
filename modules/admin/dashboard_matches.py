from models.database import db
from models.models import Match
from models.tables.event import Event
from models.tables.player import Player
from models.tables.users import Users
from itertools import chain


def get_matches_details():
    """
    Gets all the matches using the filter match status for admin view
    :return: upcoming, in progres, finished matches
    """
    db.session.expire_all()
    upcoming_matches = Match.query.filter_by(match_status='upcoming').all()
    in_progress_matches = Match.query.filter_by(match_status='in progress').all()
    finished_matches = Match.query.filter_by(match_status='finished').all()

    in_progress_match_details = []
    in_progress_and_upcoming_matches = chain(in_progress_matches, upcoming_matches)

    for match in in_progress_and_upcoming_matches:
        match_detail = {}
        match_detail['id'] = match.match_id
        match_detail['court_no'] = "" if not match.court_no else match.court_no
        print(match.court_no)
        print()
        print()
        event = Event.query.get(match.event_id)
        match_detail['event'] = event.event_name
        match_detail['event'] = match.event.event_name
        if match.result:
            match_detail['score'] = match.result.result_score
        else:
            match_detail['score'] = ''
        match_detail['status'] = match.match_status
        players_side_one = []
        for player_id in [match.side_one_player_1, match.side_one_player_2]:

            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_one.append(player_name)
        players_side_two = []
        for player_id in [match.side_two_player_1, match.side_two_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_two.append(player_name)


        side_one_players = " , ".join(players_side_one[:2]) if len(players_side_one) == 2 else players_side_one[0]
        side_two_players = " , ".join(players_side_two[:2]) if len(players_side_two) == 2 else players_side_two[0]
        match_detail['match_up'] = f"{side_one_players} vs. {side_two_players}"
        in_progress_match_details.append(match_detail)

    finished_match_details = []
    for match in finished_matches:
        match_detail = {}
        match_detail['id'] = match.match_id
        match_detail['event'] = match.event.event_name
        match_detail['score'] = match.result.result_score
        match_detail['court_no'] = "" if not match.court_no else match.court_no
        match_detail['status'] = match.match_status
        players_side_one = []
        for player_id in [match.side_one_player_1, match.side_one_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_one.append(player_name)
        players_side_two = []
        for player_id in [match.side_two_player_1, match.side_two_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_two.append(player_name)


        side_one_players = " , ".join(players_side_one[:2]) if len(players_side_one) == 2 else players_side_one[0]
        side_two_players = " , ".join(players_side_two[:2]) if len(players_side_two) == 2 else players_side_two[0]
        match_detail['match_up'] = f"{side_one_players} vs. {side_two_players}"

        winner_1 = Player.query.filter_by(player_id=match.result.winner_player_1).first()
        winner_1_user = Users.query.get(winner_1.player_id)
        winner_name = f"{winner_1_user.first_name} {winner_1_user.last_name}"

        if match.result.winner_player_2:
            winner_2 = Player.query.filter_by(player_id=match.result.winner_player_2).first()
            winner_2_user = Users.query.get(winner_2.player_id)
            winner_name += f" / {winner_2_user.first_name} {winner_2_user.last_name}"
        match_detail['winner'] = winner_name
        finished_match_details.append(match_detail)

    return {"in_progress_matches": in_progress_match_details, "finished_matches": finished_match_details}


def set_matches_court_no_and_status(request):
    """
    Sets the court number and status of a match against a match ID in the match table
    :param request: data from the front end of admin/matches page
    :return: nothing, just commits the data to the database
    """
    print(request.form.lists())
    for field, values in request.form.lists():
        if field == 'match_id':
            match_id_list = values
        elif field == 'court_no':
            court_no_list = values
        elif field == 'match_status':
            match_status_list = values

    for i in range(len(match_id_list)):
        match_id = match_id_list[i]
        court_no = court_no_list[i]
        match_status = match_status_list[i]
        match = Match.query.get(match_id)
        if match:
            if court_no:
                match.court_no = court_no
            if match_status:
                match.match_status = match_status
            db.session.commit()


def set_matches_result(request):
    """
    This method is supposed to create a result in result table, and update the match table with this result id
    :param request:
    :return:
    """
    print(request.form.lists())
    # TO DO
    # Create a new result row in the result table, and get its ID
    # Update the match table and set this result ID against the match ID
    # Handle results participants
    return


def get_public_matches_details():
    """
    Gets all the matches using the filter match status for public view
    :return: upcoming, in progres, finished matches
    """
    db.session.expire_all()
    upcoming_matches = Match.query.filter_by(match_status='upcoming').all()
    in_progress_matches = Match.query.filter_by(match_status='in progress').all()
    finished_matches = Match.query.filter_by(match_status='finished').all()

    print(upcoming_matches[1].side_two_player_1)
    upcoming_match_details = []
    in_progress_match_details = []
    finished_match_details = []

    for match in upcoming_matches:
        match_detail = {}
        match_detail['id'] = match.match_id
        match_detail['event'] = match.event.event_name

        players_side_one = []
        for player_id in [match.side_one_player_1, match.side_one_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_one.append(player_name)
        players_side_two = []
        for player_id in [match.side_two_player_1, match.side_two_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_two.append(player_name)

        side_one_players = ""
        side_two_players = ""
        if players_side_one:
            side_one_players = " , ".join(players_side_one[:2]) if len(players_side_one) == 2 else players_side_one[0]
        if players_side_two:
            side_two_players = " , ".join(players_side_two[:2]) if len(players_side_two) == 2 else players_side_two[0]
        match_detail['match_up'] = f"{side_one_players} vs. {side_two_players}"

        upcoming_match_details.append(match_detail)

    print(upcoming_match_details)

    for match in in_progress_matches:
        match_detail = {}
        match_detail['id'] = match.match_id
        match_detail['event'] = match.event.event_name
        match_detail['court_no'] = "" if not match.court_no else match.court_no

        players_side_one = []
        for player_id in [match.side_one_player_1, match.side_one_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_one.append(player_name)
        players_side_two = []
        for player_id in [match.side_two_player_1, match.side_two_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_two.append(player_name)

        side_one_players = ""
        side_two_players = ""
        if players_side_one:
            side_one_players = " , ".join(players_side_one[:2]) if len(players_side_one) == 2 else players_side_one[0]
        if players_side_two:
            side_two_players = " , ".join(players_side_two[:2]) if len(players_side_two) == 2 else players_side_two[0]
        match_detail['match_up'] = f"{side_one_players} vs. {side_two_players}"

        in_progress_match_details.append(match_detail)

    for match in finished_matches:
        match_detail = {}
        match_detail['id'] = match.match_id
        match_detail['event'] = match.event.event_name
        match_detail['score'] = match.result.result_score
        match_detail['court_no'] = "" if not match.court_no else match.court_no
        match_detail['status'] = match.match_status
        players_side_one = []
        for player_id in [match.side_one_player_1, match.side_one_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_one.append(player_name)
        players_side_two = []
        for player_id in [match.side_two_player_1, match.side_two_player_2]:
            if player_id:
                player = Player.query.get(player_id)
                user = Users.query.get(player.player_id)
                player_name = f"{user.first_name} {user.last_name}"
                players_side_two.append(player_name)

        side_one_players = ""
        side_two_players = ""
        if players_side_one:
            side_one_players = " , ".join(players_side_one[:2]) if len(players_side_one) == 2 else players_side_one[0]
        if players_side_two:
            side_two_players = " , ".join(players_side_two[:2]) if len(players_side_two) == 2 else players_side_two[0]
        match_detail['match_up'] = f"{side_one_players} vs. {side_two_players}"

        winner_1 = Player.query.filter_by(player_id=match.result.winner_player_1).first()
        winner_1_user = Users.query.get(winner_1.player_id)
        winner_name = f"{winner_1_user.first_name} {winner_1_user.last_name}"

        if match.result.winner_player_2:
            winner_2 = Player.query.filter_by(player_id=match.result.winner_player_2).first()
            winner_2_user = Users.query.get(winner_2.player_id)
            winner_name += f" / {winner_2_user.first_name} {winner_2_user.last_name}"
        match_detail['winner'] = winner_name
        finished_match_details.append(match_detail)

        print(finished_match_details)

    return {"upcoming_matches": upcoming_match_details, "in_progress_matches": in_progress_match_details,
            "finished_matches": finished_match_details}
