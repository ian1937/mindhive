from django.test import TestCase
from rest_framework.test import APIClient

from roster.models import Role, Shift, Employee, Availability
from roster.views import role_views, shift_views, employee_views, availability_views


class BaseTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        pass