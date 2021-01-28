from roster.tests import BaseTest

from roster.models import Role
from roster.views.role_views import roles, role


roles_list = [
    {'name': 'Backend Developer'},
    {'name': 'Frontend Developer'},
    {'name': 'Fullstack Developer'},
]

class RoleBaseTest(BaseTest):

    def setUp(self):
        super().setUp()

        for role in roles_list:
            role_obj = Role(name=role['name'])
            role_obj.save()

    def tearDown(self):
        Role.objects.all().delete()


class RolesEndpointTest(RoleBaseTest):

    def test_roles_endpoint(self):
        response = self.client.get('/roles/')
        self.assertEqual(response.resolver_match.func, roles)

    def test_get_return_data(self):
        response = self.client.get('/roles/')
        self.assertIn(b'Backend Developer', response.content)
        self.assertIn(b'Frontend Developer', response.content)
        self.assertIn(b'Fullstack Developer', response.content)

    def test_post_data_saved(self):
        payload = {'name': 'Project Manager'}
        response = self.client.post('/roles/', payload)
        self.assertIn(b'Project Manager', response.content)

    def test_delete_all_data(self):
        response = self.client.delete('/roles/')
        self.assertEqual(b'', response.content)


class RoleEndPointTest(RoleBaseTest):

    def test_role_endpoint(self):
        response = self.client.get('/roles/1')
        self.assertEqual(response.resolver_match.func, role)

    def test_get_return_data(self):
        response = self.client.get('/roles/1')
        role_name = response.data["name"]
        list_of_role = b"Backend Developer, Frontend Developer, Fullstack Developer"
        self.assertIn(bytes(role_name, encoding='utf-8'), list_of_role)