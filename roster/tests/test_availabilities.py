from roster.tests import BaseTest

from roster.models import Availability
from roster.views import availabilities
from roster.tests.test_employees import employees_list


availabilities_list = [
    {
        "day": "Monday",
        "start_time": "06:00",
        "end_time": "18:00"
    },
    {
        "day": "Monday",
        "start_time": "06:00",
        "end_time": "22:00"
    },
    {
        "day": "Tuesday",
        "start_time": "06:00",
        "end_time": "12:00"
    },
]

class AvailabilitiesEndpointTest(BaseTest):

    def setUp(self):
        super().setUp()

        for count, availability in enumerate(availabilities_list):
            employee = Employee(name=employees_list[count]["name"])
            availability_obj = Availability(day=availability["day"],
                                            start_time=availability["start_time"],
                                            end_time=availability["end_time"],
                                            employee=employee)
            employee.save()
            availability_obj.save()
    
    def test_availabilities_endpoint(self):
        response = self.client.get('/availabilities/')
        self.assertEqual(response.resolver_match.func, availabilities)