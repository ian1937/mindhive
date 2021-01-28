from roster.tests import BaseTest

from roster.models import Shift
from roster.views.shift_views import shifts, shift


shifts_list = [
    {
        "day": "Monday",
        "start_time": "06:00",
        "end_time": "14:00"
    },
    {
        "day": "Tuesday",
        "start_time": "06:00",
        "end_time": "14:00"
    },
    {
        "day": "Wednesday",
        "start_time": "14:00",
        "end_time": "22:00"
    },
]


class ShiftBaseTest(BaseTest):

    def setUp(self):
        super().setUp()

        for shift in shifts_list:
            shift_obj = Shift(day=shift["day"], start_time=shift["start_time"], end_time=shift["end_time"])
            shift_obj.save()


class ShiftsEndpointTest(ShiftBaseTest):

    def test_shifts_endpoint(self):
        response = self.client.get('/shifts/')
        self.assertEqual(response.resolver_match.func, shifts)

    def test_get_return_data(self):
        response = self.client.get('/shifts/')
        self.assertIn(b'Monday', response.content)
        self.assertIn(b'Tuesday', response.content)

    def test_post_data_saved(self):
        payload = {"day": "Wednesday", "start_time": "14:00", "end_time": "22:00"}
        response = self.client.post('/shifts/', payload)
        self.assertIn(b'Wednesday', response.content)

    def test_delete_all_data(self):
        response = self.client.delete('/shifts/')
        self.assertEqual(b'', response.content)


class ShiftEndpointTest(ShiftBaseTest):

    def test_shift_endpoint(self):
        response = self.client.get("/shifts/1")
        self.assertEqual(response.resolver_match.func, shift)

    def test_get_return_data(self):
        response = self.client.get("/shifts/1")
        shift_day = response.data["day"]
        list_of_shift_day = b"Monday, Tuesday"
        self.assertIn(bytes(shift_day, encoding="utf-8"), list_of_shift_day)

    def test_put_data_changed(self):
        # Get current shift's day (should be "Monday")
        get_response = self.client.get("/shifts/1")
        get_shift_day = get_response.data["day"]
        # Change day to "Friday"
        payload = {"day": "Friday", "start_time": "06:00", "end_time": "14:00"}
        response = self.client.put("/shifts/1", payload)
        # Get changed day
        shift_day = response.data["day"]
        # Changed day should be in response
        self.assertIn(b"Friday", response.content)
        # Old day should not be in response
        self.assertNotIn(bytes(get_shift_day, encoding="utf-8"), response.content)

    def test_delete_data(self):
        response = self.client.delete("/shifts/1")
        self.assertEqual(b"", response.content)
