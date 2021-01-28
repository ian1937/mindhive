from roster.tests import BaseTest

from roster.models import Role
from roster.views.role_views import roles, role


roles_list = [
    {"name": "Backend Developer"},
    {"name": "Frontend Developer"},
    {"name": "Fullstack Developer"},
    {"name": "Project Manager"},
    {"name": "Scrum Master"},
    {"name": "QA Engineer"},
    {"name": "Devops"},
]

class RoleBaseTest(BaseTest):

    def setUp(self):
        super().setUp()

        for role in roles_list:
            role_obj = Role(name=role["name"])
            role_obj.save()


class RolesEndpointTest(RoleBaseTest):

    def test_roles_endpoint(self):
        response = self.client.get("/roles/")
        self.assertEqual(response.resolver_match.func, roles)

    def test_get_return_data(self):
        response = self.client.get("/roles/")
        self.assertIn(b"Backend Developer", response.content)
        self.assertIn(b"Frontend Developer", response.content)
        self.assertIn(b"Fullstack Developer", response.content)

    def test_post_data_saved(self):
        payload = {"name": "Project Manager"}
        response = self.client.post("/roles/", payload)
        self.assertIn(b"Project Manager", response.content)

    def test_delete_all_data(self):
        response = self.client.delete("/roles/")
        self.assertEqual(b"", response.content)


class RoleEndPointTest(RoleBaseTest):

    def test_role_endpoint(self):
        response = self.client.get("/roles/1")
        self.assertEqual(response.resolver_match.func, role)

    def test_get_return_data(self):
        response = self.client.get("/roles/1")
        role_name = response.data["name"]
        list_of_role_name = b"Backend Developer, Frontend Developer, Fullstack Developer"
        self.assertIn(bytes(role_name, encoding="utf-8"), list_of_role_name)

    def test_put_data_changed(self):
        # Get current name (should be "Backend Developer")
        get_response = self.client.get("/roles/1")
        get_role_name = get_response.data["name"]
        # Change name to "Python Developer"
        payload = {"name": "Python Developer"}
        response = self.client.put("/roles/1", payload)
        # Get changed name
        role_name = response.data["name"]
        # Changed Name should be in response
        self.assertIn(b"Python Developer", response.content)
        # Old name should not be in response
        self.assertNotIn(bytes(get_role_name, encoding="utf-8"), response.content)

    def test_delete_data(self):
        response = self.client.delete("/roles/1")
        self.assertEqual(b"", response.content)
    