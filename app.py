from flask import *
from models.models import db
from flask_migrate import Migrate

from modules.web.routes import web_app
from modules.user.routes import user_app
from modules.admin.routes import admin_app
from modules.player.routes import player_app

''' App Config '''
app = Flask(__name__)
app.secret_key = 'csc536'

'''Database setup'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:uabadmintontournamentadmin@uabadmintontournament' \
                                        '.cw5ilorod8lo.us-east-2.rds.amazonaws.com:5432/uabadmintontournamentdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
'''Route management'''

app.register_blueprint(web_app)
app.register_blueprint(user_app)
app.register_blueprint(admin_app)
app.register_blueprint(player_app)

db.init_app(app)
migrate = Migrate(app, db)
