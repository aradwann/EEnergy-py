from rest_framework.test import APITestCase
from ..models import EnergyResource
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point

point = Point(-8, 8)


class EnergyResourcesModelTests(APITestCase):

    def setUp(self):
        # create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword")

    def test_create_energy_resource(self):
        """
        Ensure we can create a new energy_resource object
        """

        resource = EnergyResource.objects.create(
            resource_type="wind farm",
            status="active",
            location=point,
            capacity=18.0,
            consumption=12.0,
            net_energy=6.0,
            owner=self.user
        )
        resource_str = f'{resource.owner.username}\'s {resource.resource_type}'

        self.assertEqual(EnergyResource.objects.count(), 1)
        self.assertEqual(EnergyResource.objects.get().id, resource.id)
        self.assertEqual(
            EnergyResource.objects.get().resource_type, resource.resource_type)
        self.assertEqual(EnergyResource.objects.get().status,
                         resource.status)
        self.assertEqual(
            EnergyResource.objects.get().location, resource.location)
        self.assertEqual(EnergyResource.objects.get().capacity,
                         resource.capacity)
        self.assertEqual(EnergyResource.objects.get(
        ).net_energy, resource.net_energy)
        self.assertEqual(str(resource), resource_str)
