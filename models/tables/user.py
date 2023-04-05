from app import db


class User(db.Model):
    """
    Class User: Users consist of Admin and Players, this table stores infromation relation to users
    Player specific information is stored in 'Player' child class
    Permissions for Admin and Players are stored in 'Permission' child class
    Login credentials for Admin and Players are stored in 'Login' class
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    login_id = db.Column(db.String(50), db.ForeignKey('login.login_id'))
    #player = db.relationship('Player', backref='user', lazy=True)
    #user_permission = db.relationship('UserPermission', backref='user', lazy=True)

    def __init__(self, first_name, email, last_name=None):
        """
        Constructor for User Table
        :param first_name: First name of the user
        :param last_name: Last name of the user
        :param email: Email of the user
        :param user_id: User ID of the user
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', email='%s')>" % \
            (self.first_name, self.last_name, self.email)
