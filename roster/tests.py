from django.test import TestCase
from rest_framework.test import APIClient

from roster.models import Role, Shift, Employee, Availability
from roster.views import roles, shifts, employees, availabilities


class BaseTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass


class RoleEndpointTest(BaseTest):

    def setUp(self):
        super().setUp()
        roles = [
            {'name': 'Fullstack Developer'},
            {'name': 'Frontend Developer'},
            {'name': 'Backend Developer'},
        ]
        for role in roles:
            role_obj = Role(name=role['name'])
            role_obj.save()

    def test_endpoint(self):
        response = self.client.get('/roles/')
        self.assertEqual(response.resolver_match.func, roles)

    def test_get_return_data(self):
        response = self.client.get('/roles/')
        self.assertIn(b'Backend Developer', response.content)

    def test_post_status_code(self):
        payload = {'name': 'QA Engineer'}
        response = self.client.post('/roles/', payload)
        self.assertEqual(response.status_code, 201)

    def test_post_data_saved(self):
        payload = {'name': 'Project Manager'}
        response = self.client.post('/roles/', payload)
        self.assertIn(b'Project Manager', response.content)

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
