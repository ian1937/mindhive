from roster.tests import BaseTest

from roster.models import Employee, Role
from roster.views import employees
from roster.tests.test_roles import roles_list


employees_list = [
    {"name": "Donna Valentina"},
    {"name": "Daniel Kanasimo"},
    {"name": "Ricky Sudargo"},
]

class EmployeesEndpointTest(BaseTest):

    def setUp(self):
        super().setUp()

        for count, employee in enumerate(employees_list):
            role = Role.objects.filter(name=roles_list[count]["name"]).first()
            employee_obj = Employee(name=employee["name"], role=role)
            employee_obj.save()
    
    def test_employees_endpoint(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.resolver_match.func, employees)