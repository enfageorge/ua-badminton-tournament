from app import db

"""
Class Permission: Stores rwx permissions for Admins and Players
"""


class Permission(db.Model):
    __tablename__ = "permission"
    id = db.Column(db.Integer, primary_key=True)
    read = db.Column(db.Boolean, nullable=False)
    write = db.Column(db.Boolean, nullable=False)
    delete = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('permission.id'))

    def __init__(self, id: int , read: bool, write: bool, delete: bool, user_id=None):
        """
        Constructor for Permission Table
        :param id: Primary Key for the Permission Table
        :param read: Data read permission
        :param write: Data write permission
        :param delete: Data delete permission
        :param user_id: Foreign Key for User Table
        """
        self.id = id
        self.read = read
        self.write = write
        self.delete = delete
        self.user_id = user_id

    def __repr__(self):
        return "<Permissions(id='%s', read='%s', write='%s', delete'%s')>" % (
            self.id, self.read, self.write, self.delete)
