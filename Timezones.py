from TimezonesList import TimezonesList
from flask_restful import Resource

timezonesList = TimezonesList()
class Timezones(Resource):
    def get(self):
        timezones = timezonesList.getTimeZones()  
        for timezone in timezones:
            timezone['links'] = [{
            'rel': 'self',
            'uri': '/timezones/' + str(timezone['id'])}]
        return { 'data' : timezones, 'status': 200, 'error': 'False'}