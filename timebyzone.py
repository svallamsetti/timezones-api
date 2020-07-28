from datetime import datetime

def retrieveTimeInGivenZone(UTCOffset):
        numberOfHours = UTCOffset[1:]
        if ':' in numberOfHours:
            timeInHoursAndMinutes = numberOfHours.split(":")
            timeUTCOffsetInMicroSeconds = int(timeInHoursAndMinutes[0]) * 3600000 + int(timeInHoursAndMinutes[-1]) * 60000
        else:
            timeUTCOffsetInMicroSeconds = int(numberOfHours) * 3600000
        timeInMicroSeconds = int(datetime.utcnow().strftime("%s")) * 1000
        if UTCOffset[0] == '-':
            currentTimeInMilliseconds =  timeInMicroSeconds - timeUTCOffsetInMicroSeconds
        else:
            currentTimeInMilliseconds =  timeInMicroSeconds + timeUTCOffsetInMicroSeconds
        seconds = (currentTimeInMilliseconds//1000)%60
        minutes = (currentTimeInMilliseconds//(1000*60))%60
        hours = (currentTimeInMilliseconds//(1000*60*60))%24
        twentyFourHourFormat = str(hours).zfill(2) + ':'+ str(minutes).zfill(2) +':'+ str(seconds).zfill(2)
        hoursList = {
          12: 12,
          13: 1,
          14: 2,
          15: 3,
          16: 4,
          17: 5,
          18: 6,
          19: 7,
          20: 8,
          21: 9,
          22: 10,
          23: 11,
        }        
        meridian = 'AM'
        if hours >= 12:
          hours = hoursList[hours]
          meridian = 'PM'
        elif hours == 0:
          hours = 12    
        time = str(hours).zfill(2) + ':'+ str(minutes).zfill(2) +':'+ str(seconds).zfill(2) +' '+ meridian
        return {'time':time, 'twentyFourHourFormat': twentyFourHourFormat}