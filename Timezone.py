from TimezonesList import TimezonesList
from flask_restful import Resource
import timebyzone

timezonesList = TimezonesList()
class Timezone(Resource):
    def get(self, timezoneId):
        timezoneObject = next(filter(lambda timezone: timezone['id'] == timezoneId, timezonesList.getTimeZones()), None)
        if timezoneObject:
            timezoneObject['currentTime'] = timebyzone.retrieveTimeInGivenZone(timezoneObject['UTCOffset'])['time']
            timezoneObject['currentTimeIn24Hr'] = timebyzone.retrieveTimeInGivenZone(timezoneObject['UTCOffset'])['twentyFourHourFormat']
            return { 'data': timezoneObject, 'status' : 200, 'error': 'False' }
        return { 'data': {'message' : 'Requested resource not found'}, 'status' : 404, 'error': 'True' }