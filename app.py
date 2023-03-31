from flask import *
# from flask_sqlalchemy import SQLAlchemy

from modules.web.routes import web_app
from modules.user.routes import user_app
from modules.admin.routes import admin_app
from modules.player.routes import player_app

''' App Config '''
app = Flask(__name__)
app.secret_key = 'csc536'

'''Database setup'''

# app.config['SQLALCHEMY_DATABASE_URI'] = 'PLACEHOLDER'  # TBA
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

'''Route management'''

app.register_blueprint(web_app)
app.register_blueprint(user_app)
app.register_blueprint(admin_app)
app.register_blueprint(player_app)
