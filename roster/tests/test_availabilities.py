from roster.tests import BaseTest

from roster.models import Availability, Employee, Role
from roster.views.availability_views import availabilities, availability
from roster.tests.test_employees import employees_list
from roster.tests.test_roles import roles_list


availabilities_list = [
    {
        "day": "Monday",
        "start_time": "06:00",
        "end_time": "18:00"
    },
    {
        "day": "Tuesday",
        "start_time": "06:00",
        "end_time": "22:00"
    },
    {
        "day": "Wednesday",
        "start_time": "06:00",
        "end_time": "12:00"
    },
    {
        "day": "Thursday",
        "start_time": "06:00",
        "end_time": "16:00"
    },
    {
        "day": "Friday",
        "start_time": "08:00",
        "end_time": "12:00"
    },
    {
        "day": "Saturday",
        "start_time": "06:00",
        "end_time": "20:00"
    },
    {
        "day": "Sunday",
        "start_time": "10:00",
        "end_time": "22:00"
    },
]


class AvailabilityBaseTest(BaseTest):

    def setUp(self):
        super().setUp()

        for count, availability in enumerate(availabilities_list):
            role = Role(name=roles_list[count]["name"])
            role.save()
            employee = Employee(name=employees_list[count]["name"], role=role)
            employee.save()
            availability_obj = Availability(day=availability["day"],
                                            start_time=availability["start_time"],
                                            end_time=availability["end_time"],
                                            employee=employee)
            availability_obj.save()


class AvailabilitiesEndpointTest(AvailabilityBaseTest):
    
    def test_availabilities_endpoint(self):
        response = self.client.get('/availabilities/')
        self.assertEqual(response.resolver_match.func, availabilities)

    def test_get_return_data(self):
        response = self.client.get("/availabilities/")
        self.assertIn(b"Monday", response.content)
        self.assertIn(b"Tuesday", response.content)
        self.assertIn(b"Wednesday", response.content)

    def test_post_data_saved(self):
        role = Role(name="Project Manager")
        role.save()
        employee = Employee(name="Patricia Carolina", role=role)
        employee.save()
        payload = {"day": "Sunday", 
                    "start_time": "06:00", 
                    "end_time": "18:00", 
                    "employee": employee.id}
        response = self.client.post("/availabilities/", payload)
        self.assertIn(b"Sunday", response.content)
        self.assertIn(b"Patricia Carolina", response.content)

    def test_delete_all_data(self):
        response = self.client.delete("/availabilities/")
        self.assertEqual(b"", response.content)


class AvailabilityEndpointTest(AvailabilityBaseTest):

    def test_availability_endpoint(self):
        response = self.client.get("/availabilities/1")
        self.assertEqual(response.resolver_match.func, availability)

    def test_get_return_data(self):
        response = self.client.get("/availabilities/1")
        availability_day = response.data["day"]
        list_of_availability_day = b"Monday, Tuesday, Wednesday"
        self.assertIn(bytes(availability_day, encoding="utf-8"), list_of_availability_day)

    def test_put_data_changed(self):
        # Get current day (should be "Monday")
        get_response = self.client.get("/availabilities/1")
        get_availability_day = get_response.data["day"]
        # Change day to "Friday"
        payload = {"day": "Friday", "start_time": "06:00", "end_time": "14:00"}
        response = self.client.put("/availabilities/1", payload)
        # Get changed day
        availability_day = response.data["day"]
        # Changed day should be in response
        self.assertIn(b"Friday", response.content)
        # Old day should not be in response
        self.assertNotIn(bytes(get_availability_day, encoding="utf-8"), response.content)

    def test_delete_data(self):
        response = self.client.delete("/availabilities/1")
        self.assertEqual(b"", response.content)
