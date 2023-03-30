from app import db
from sqlalchemy import ForeignKey
from datetime import datetime
"""
Class Match, stores information relation to match that belongs to a Tournament and an Event
"""


class Match(db.Model):
    __tablename__ = "match"
    match_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, default=datetime.utcnow())
    side_one_player_1 = db.Column(db.Integer, ForeignKey('player.id'), nullable=False)
    side_one_player_2 = db.Column(db.Integer, ForeignKey('player.id'), nullable=True)
    side_two_player_1 = db.Column(db.Integer, ForeignKey('player.id'), nullable=False)
    side_two_player_2 = db.Column(db.Integer, ForeignKey('player.id'), nullable=True)
    tournament_id = db.Column(db.Integer, ForeignKey('tournament.tournament_id'), nullable=False)
    event_id = db.Column(db.Integer, ForeignKey('event.event_id'), nullable=False)
    result_id = db.Column(db.Integer, ForeignKey('result.result_id'), nullable=True)

    def __init__(self, date: str, side_one_player_1: int, side_two_player_1: int, tournament_id: int, event_id: int,
                 result_id: int = None, side_one_player_2: int = None, side_two_player_2: int = None) -> None:
        """
        Initialize a Match object with the given attributes.
        date: The date of the match in MM-DD-YYYY format.
        side_one_player_1: The player id of the first player on side one.
        side_one_player_2: The player id of the second player on side one.
        side_two_player_1: The player id of the first player on side two.
        side_two_player_2: The player id of the second player on side two.
        tournament_id: The id of the tournament this match was played in.
        event_id: The id of the event this match was played in.
        result_id: The id of the result of this match.
        """
        self.date = date
        self.side_one_player_1 = side_one_player_1
        self.side_one_player_2 = side_one_player_2
        self.side_two_player_1 = side_two_player_1
        self.side_two_player_2 = side_two_player_2
        self.tournament_id = tournament_id
        self.event_id = event_id
        self.result_id = result_id

        def __repr__(self):
            return f"<Match(match_id={self.match_id}, date={self.date}, side_one_player_1={self.side_one_player_1}," \
                   f" side_one_player_2={self.side_one_player_2}, side_two_player_1={self.side_two_player_1}," \
                   f" side_two_player_2={self.side_two_player_2}, tournament_id={self.tournament_id}," \
                   f" event_id={self.event_id}, result_id={self.result_id})>"
