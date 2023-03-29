from flask import *
# from flask_sqlalchemy import SQLAlchemy

from modules.web.routes import web_app
from modules.admin.routes import admin_app
from modules.user_management.routes import user_management_app

''' App Config '''
app = Flask(__name__)
app.secret_key = 'csc536'

'''Database setup'''

# app.config['SQLALCHEMY_DATABASE_URI'] = 'PLACEHOLDER'  # TBA
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

'''Route management'''

app.register_blueprint(user_management_app)
app.register_blueprint(admin_app)
app.register_blueprint(web_app)
