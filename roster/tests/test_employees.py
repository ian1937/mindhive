from roster.tests import BaseTest

from roster.models import Employee
from roster.views import employees


class EmployeesEndpointTest(BaseTest):
    
    def test_employees_endpoint(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.resolver_match.func, employees)