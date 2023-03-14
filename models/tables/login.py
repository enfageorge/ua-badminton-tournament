from app import db

"""
Class Login stores Login information related to Users (Admin and Players)
"""


class Login(db.Model):
    __tablename__ = "login"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, id: int, password: str, user_id=None):
        self.id = id
        self.password = password
        self.user_id = user_id

    def __repr__(self):
        return "<Login(first_name='%s', last_name='%s', competing_gender'%s')>" % (
            self.first_name, self.last_name, self.competing_gender)
