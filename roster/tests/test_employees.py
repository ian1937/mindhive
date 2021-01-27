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
        response = self.client.get("/employees/")
        self.assertEqual(response.resolver_match.func, employees)

    def test_get_return_data(self):
        response = self.client.get("/employees/")
        self.assertIn(b"Donna Valentina", response.content)
        self.assertIn(b"Daniel Kanasimo", response.content)
        self.assertIn(b"Ricky Sudargo", response.content)

    # def test_post_data_saved(self):
    #     role = Role.objects.first()
    #     payload = {"name": "Patricia Carolina", "role": role}
    #     response = self.client.post("/employees/", payload)
    #     self.assertIn(b"Patricia Carolina", response.content)
    #     self.assertIn(b"Project Manager", response.content)

    def test_delete_all_data(self):
        response = self.client.delete("/employees/")
        self.assertEqual(b"", response.content)