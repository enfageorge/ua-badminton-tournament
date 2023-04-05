from datetime import datetime
from app import db

"""
Class Player, stores information relation to badminton players
"""


class Player(db.Model):
    __tablename__ = "player"
    player_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    seeding_score = db.Column(db.Integer, nullable=True)
    social_media_consent = db.Column(db.Boolean, nullable=False)
    competing_gender = db.Column(db.String(10), nullable=True)
    phone_number = db.Column(db.String(10), nullable=True)
    dob = db.Column(db.Date, default=datetime.utcnow())
    club_name = db.Column(db.String(30), nullable=True)

    # matches = db.relationship('Match', backref='player', lazy=True)
    # event_player = db.relationship('EventPlayer', backref='player', lazy=True)

    def __init__(self, player_id: int, seeding_score: int, social_media_consent: bool, competing_gender: str,
                 phone_number: str, dob: str, club_name: str):
        """
        Constructor for Player Table
        :param player_id: Primary for the Player Table, FK references Users table
        :param seeding_score: the seeding score based on which players are ranked
        :param social_media_consent: if True, player agrees for photography/videography
        :param competing_gender: Determines eligibility for playing in competing gender specific matches
        :param phone_number: contact number
        :param dob: determines age
        :param club_name: the name of the club player belongs to
        """
        self.player_id = player_id
        self.seeding_score = seeding_score
        self.social_media_consent = social_media_consent
        self.competing_gender = competing_gender
        self.phone_number = phone_number
        self.dob = dob
        self.club_name = club_name

    def __repr__(self):
        return "<Player(player_id='%s', competing_gender'%s')>" % (
            self.player_id, self.competing_gender)
