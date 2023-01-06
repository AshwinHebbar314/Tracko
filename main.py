"""
WHERE ALL THE MAGIC HAPPENS, MAIN METHOD
"""

import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from application.database import db 
from flask_login import LoginManager
from flask_restful import Api

app = None
api = None

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'sicrit'
db = SQLAlchemy(app)
api = Api(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.app_context().push()


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


from application.methods import * 
@app.route('/favicon.ico') 
def favicon(): 
    """FAVICON"""
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

#############################################################################################################
# PASSING API ENDPOINTS
from application.api import TrackerListAPI
api.add_resource(TrackerListAPI, '/api/trackers/<string:username>')

from application.api import LogAPI
api.add_resource(LogAPI, '/api/log/<string:trackerid>','/api/log/delete/<string:logid>')
#############################################################################################################

# RUNNING THE APP ITSELF
if __name__ == '__main__':
  app.debug = True
  app.run() 