from roster.tests import BaseTest

from roster.models import Availability
from roster.views import availabilities


class AvailabilitiesEndpointTest(BaseTest):
    
    def test_availabilities_endpoint(self):
        response = self.client.get('/availabilities/')
        self.assertEqual(response.resolver_match.func, availabilities)