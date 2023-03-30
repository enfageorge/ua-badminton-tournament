from app import db

"""
Class representing the match-player participation table, with a many-to-many relationship between matches & players.
"""


class MatchPlayerParticipation(db.Model):
    __tablename__ = 'match_player_participation'
    match_id = db.Column(db.Integer, db.ForeignKey('match.match_id'), primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), primary_key=True)

    def __repr__(self) -> str:
        """
        Returns a string representation of the MatchPlayerParticipation object.
        """
        return f'<MatchPlayerParticipation Match ID={self.match_id} - PlayerID={self.player_id}>'
