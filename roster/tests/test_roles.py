from roster.tests import BaseTest

from roster.models import Role
from roster.views import roles


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

    def test_delete_all_data(self):
        response = self.client.delete('/roles/')
        self.assertEqual(b'', response.content)