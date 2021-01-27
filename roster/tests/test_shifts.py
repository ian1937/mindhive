from roster.tests import BaseTest

from roster.models import Shift
from roster.views import shifts


class ShiftsEndpointTest(BaseTest):

    def setUp(self):
        super().setUp()
        shifts = [
            {
                "day": "Monday",
                "start_time": "06:00",
                "end_time": "14:00"
            },
            {
                "day": "Monday",
                "start_time": "14:00",
                "end_time": "22:00"
            },
            {
                "day": "Tuesday",
                "start_time": "06:00",
                "end_time": "14:00"
            },
            {
                "day": "Tuesday",
                "start_time": "14:00",
                "end_time": "22:00"
            },
        ]
        for shift in shifts:
            shift_obj = Shift(day=shift["day"], start_time=shift["start_time"], end_time=shift["end_time"])
            shift_obj.save()

    def test_shifts_endpoint(self):
        response = self.client.get('/shifts/')
        self.assertEqual(response.resolver_match.func, shifts)

    def test_get_return_data(self):
        response = self.client.get('/shifts/')
        self.assertIn(b'Monday', response.content)