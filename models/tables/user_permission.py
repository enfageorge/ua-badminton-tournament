from app import db

"""
Class Login stores Login information related to Users (Admin and Players)
"""


class UserPermission(db.Model):
    __tablename__ = "userpermission"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), primary_key=True)

    def __init__(self, user_id, permission_id):
        self.user_id = user_id
        self.permission_id = permission_id

    def __repr__(self):
        return f"<UserPermission(user_id='{self.user_id}', permission_id='{self.permission_id}')>"

