from app import db

"""
Class Player, stores information relation to badminton players
"""


class Player(db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    seeding_score = db.Column(db.Integer, nullable=True)
    social_media_consent = db.Column(db.Boolean, nullable=False)
    competing_gender = db.Column(db.Char, nullable=False)
    phone_number = db.Column(db.String(10), nullable=True)
    dob = db.Column(db.String(10), nullable=False)  # MM-DD-YYYY
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, id: int, seeding_score: int, social_media_consent: bool, competing_gender: str,
                 phone_number: str, dob: str, user_id=None):
        """
        Constructor for Player Table
        :param id: Primary for the Player Table
        :param seeding_score: the seeding score based on which players are ranked
        :param social_media_consent: if True, player agrees for photography/videography
        :param competing_gender: Determines eligibility for playing in competing gender specific matches
        :param phone_number: contact number
        :param dob: determines age
        :param user_id: Foreign Key for User Table
        """
        self.id = id
        self.seeding_score = seeding_score
        self.seeding_score = id
        self.social_media_consent = social_media_consent
        self.competing_gender = competing_gender
        self.phone_number = phone_number
        self.dob = dob
        self.user_id = user_id

    def __repr__(self):
        return "<Player(first_name='%s', last_name='%s', competing_gender'%s')>" % (
            self.first_name, self.last_name, self.competing_gender)
