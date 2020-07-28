from timebyzone import retrieveTimeInGivenZone
from freezegun import freeze_time
import pytest

@pytest.mark.parametrize("offset,time,timeInTwentyFourHourFormat",
                        [
                            ("+5:30", "05:30:00 PM", "17:30:00"),
                            ("+12", "12:00:00 AM", "00:00:00"),
                            ("+2:00", "02:00:00 PM", "14:00:00"),
                            ("+2", "02:00:00 PM", "14:00:00"),
                            ("-2", "10:00:00 AM", "10:00:00" ),
                            ("-3:25", "08:35:00 AM", "08:35:00"),
                            ("-12", "12:00:00 AM", "00:00:00"),
                            ("+0", "12:00:00 PM", "12:00:00"),
                            ("-0", "12:00:00 PM", "12:00:00")
                        ])
def test_timeByOffsetToUTC(offset, time, timeInTwentyFourHourFormat):
    freezer = freeze_time('2020-07-27 12:00:00')
    freezer.start()
    assert retrieveTimeInGivenZone(offset)['time'] == time
    assert retrieveTimeInGivenZone(offset)['twentyFourHourFormat'] == timeInTwentyFourHourFormat
    freezer.stop()