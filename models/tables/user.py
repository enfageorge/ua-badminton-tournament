from app import db

"""
Class User: Users consist of Admin and Players, this table stores infromation relation to users
Player specific information is stored in 'Player' child class
Permissions for Admin and Players are stored in 'Permission' child class
Login credentials for Admin and Players are stored in 'Login' class
"""


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    is_player = db.Relationship('Player', uselist=False)
    permission = db.Relationship('Permission', uselist=False)
    login = db.Relationship('Login', uselist=False)

    def __init__(self, id, first_name, last_name, email, is_player=None, permission=None):
        """
        Constructor for User Table
        :param id: Primary key for the User Table
        :param first_name: first name of the user
        :param last_name: last name of the user
        :param email: email of the user
        :param is_player: determines if the user is a player
        :param permission: permissions for the user
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_player = is_player
        self.permission = permission

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s')>" % (self.first_name, self.last_name)
