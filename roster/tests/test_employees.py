from roster.tests import BaseTest

from roster.models import Employee, Role
from roster.views.employee_views import employees, employee
from roster.tests.test_roles import roles_list


employees_list = [
    {"name": "Donna Valentina"},
    {"name": "Daniel Kanasimo"},
    {"name": "Ricky Sudargo"},
]


class EmployeeBaseTest(BaseTest):

    def setUp(self):
        super().setUp()

        for count, employee in enumerate(employees_list):
            role = Role(name=roles_list[count]["name"])
            role.save()
            employee_obj = Employee(name=employee["name"], role=role)
            employee_obj.save()


class EmployeesEndpointTest(EmployeeBaseTest):
    
    def test_employees_endpoint(self):
        response = self.client.get("/employees/")
        self.assertEqual(response.resolver_match.func, employees)

    def test_get_return_data(self):
        response = self.client.get("/employees/")
        self.assertIn(b"Donna Valentina", response.content)
        self.assertIn(b"Daniel Kanasimo", response.content)
        self.assertIn(b"Ricky Sudargo", response.content)

    def test_post_data_saved(self):
        role = Role(name="Project Manager")
        role.save()
        payload = {"name": "Patricia Carolina", "role": role.id}
        response = self.client.post("/employees/", payload)
        self.assertIn(b"Project Manager", response.content)
        self.assertIn(b"Patricia Carolina", response.content)

    def test_delete_all_data(self):
        response = self.client.delete("/employees/")
        self.assertEqual(b"", response.content)


class EmployeeEndpointTest(EmployeeBaseTest):

    def test_employee_endpoint(self):
        response = self.client.get("/employees/1")
        self.assertEqual(response.resolver_match.func, employee)

    def test_get_return_data(self):
        response = self.client.get("/employees/1")
        employee_name = response.data["name"]
        list_of_employee_name = b"Donna Valentina, Daniel Kanasimo, Ricky Sudargo"
        self.assertIn(bytes(employee_name, encoding="utf-8"), list_of_employee_name)

    def test_put_data_changed(self):
        # Get current name (should be "Donna Valentina")
        get_response = self.client.get("/employees/1")
        get_employee_name = get_response.data["name"]
        # Change name to "Dian Novick"
        payload = {"name": "Dian Novick"}
        response = self.client.put("/employees/1", payload)
        # Get changed name
        employee_name = response.data["name"]
        # Changed Name should be in response
        self.assertIn(b"Dian Novick", response.content)
        # Old name should not be in response
        self.assertNotIn(bytes(get_employee_name, encoding="utf-8"), response.content)

    def test_delete_data(self):
        response = self.client.delete("/employees/1")
        self.assertEqual(b"", response.content)
