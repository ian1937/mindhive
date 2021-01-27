from django.test import TestCase
from rest_framework.test import APIClient

from roster.views import roles, shifts, employees, availabilities


class BaseTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass


class RoleEndpointTest(BaseTest):

    def test_endpoint(self):
        response = self.client.get('/roles/')
        self.assertEqual(response.resolver_match.func, roles)

    # def test_return_data(self):
    #     endpoint = resolve('/roles')
    #     self.assertEqual(endpoint.response)


class ShiftsEndpointTest(BaseTest):

    def test_shifts_endpoint(self):
        response = self.client.get('/shifts/')
        self.assertEqual(response.resolver_match.func, shifts)


class EmployeesEndpointTest(BaseTest):
    
    def test_employees_endpoint(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.resolver_match.func, employees)


class AvailabilitiesEndpointTest(BaseTest):
    
    def test_availabilities_endpoint(self):
        response = self.client.get('/availabilities/')
        self.assertEqual(response.resolver_match.func, availabilities)
