"""
FOR THE API BASED OPERATIONS
"""

from flask_restful import Resource, reqparse
from controllers.appfunc import *
from application.models import *
import datetime



log_parser = reqparse.RequestParser()
log_parser.add_argument('value', type=str, required=True, help='Value is required')
log_parser.add_argument('description', type=str, required=False, help='Description is required')

class TrackerListAPI(Resource):
    def get(self, username):
        try:
            id = User.query.filter_by(name=username).first().id
            if id is None:
                return {'message': 'User not found'}, 404
            tracker = Tracker.query.filter_by(userid = id).all()
            l = []
            for t in tracker:
                l.append({'id': t.id, 'name': t.name})
            return l, 200
        except:
            return {'message': 'User not found'}, 404

class LogAPI(Resource):
    def post(self, trackerid):
        try:
            args = log_parser.parse_args()
            value = args.get('value')
            description = args.get('description', "")
            tracker = Tracker.query.filter_by(id = trackerid).first()
            if tracker.type in  ['2', '4', 2, 4]:
                c = tracker.choices.split()
                if value not in c:
                    return  {'message': 'Value Not Recognised'}, 404
            log = Logs(userid = tracker.userid, tid = tracker.id, value=value, data = description, time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            db.session.add(log)
            db.session.commit()
            return {'message': 'Logged  successfully'}, 200
        except:
            return {'message': 'Log not found'}, 404

    def get(self, trackerid):
        try:
            log = Logs.query.filter_by(tid = trackerid).all()
            if log is None:
                return {'message': 'Log not found'}, 404
            l = []
            for t in log:
                l.append({'id': t.id, 'value': t.value, 'description': t.data, 'time': t.time})
            return l, 200
        except:
            return {'message': 'Log not found'}, 404
    
    def delete(self, logid):
        try:
            Logs.query.filter_by(id = logid).delete()

            db.session.commit()
            return {'message': 'Log Deleted Successfully'}, 200
        except:
            return {'message': 'Log not found'}, 404