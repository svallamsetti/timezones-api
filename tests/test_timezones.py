from unittest import TestCase
import timezones

class TestTimezones(TestCase):
    def test_home_page(self):
        response = timezones.retrieveTimeInGivenZone('+4')
        self.assertTrue('23:57:06')