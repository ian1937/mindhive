from django.test import TestCase
from rest_framework.test import APIClient

from roster.models import Role, Shift, Employee, Availability
from roster.views import roles, shifts, employees, availabilities


class BaseTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass