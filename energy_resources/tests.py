from django.test import TestCase
from .models import EnergyResource
from django.contrib.auth import get_user_model


class EnergyResourcesModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a test user
        test_user1 = get_user_model().objects.create_user(
            username="testuser", password="testpassword")
        test_user1.save()

        # create a test energy resource

        test_energy_resource = EnergyResource.objects.create(
            owner=test_user1, resource_type="wind", status="active", capacity=152)

        test_energy_resource.save()

    def test_energy_resource_content(self):
        energy_resource = EnergyResource.objects.get(id=1)
        owner = f'{energy_resource.owner}'
        status = f'{energy_resource.status}'
        resource_type = f'{energy_resource.resource_type}'
        capacity = f'{energy_resource.capacity}'

        self.assertEqual(owner, 'testuser')
        self.assertEqual(resource_type, 'wind')
        self.assertEqual(status, 'active')
        self.assertEqual(capacity, '152.0')
