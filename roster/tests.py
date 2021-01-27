from django.test import TestCase
from django.urls import resolve

from roster.views import shifts, employees, availability


class EndpointTest(TestCase):
    def test_shifts_endpoint(self):
        endpoint = resolve('/shifts')
        self.assertEqual(endpoint.func, shifts)

    def test_employees_endpoint(self):
        endpoint = resolve('/employees')
        self.assertEqual(endpoint.func, employees)

    def test_availability_endpoint(self):
        endpoint = resolve('/availability')
        self.assertEqual(endpoint.func, availability)
