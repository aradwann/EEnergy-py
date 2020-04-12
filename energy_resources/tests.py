from .models import EnergyResource
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token


class EnergyResourcesModelTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # create a test user
        test_user1 = get_user_model().objects.create_user(
            username="testuser", password="testpassword")
        test_user1.save()

        # create a test energy resource
        pnt = Point(-8.789062498776527, 8.146242823908073)
        # test_energy_resource = EnergyResource.objects.create(
        # owner=test_user1, location=pnt, resource_type="wind", status="active", capacity=152)

        # test_energy_resource.save()
    '''
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
    '''

    def test_create_energy_resource(self):
        """
        Ensure we can create a new energy_resource object.
        """
        pnt = Point(-8.789062498776527, 8.146242823908073)
        url = reverse('energy-resources-list')
        data = {
            "id": 1,
            "resource_type": "wind farm",
            "status": "active",
            "location": {
                "type": "Point",
                "coordinates": [
                    -8.789062498776527,
                    8.146242823908073
                ]
            },
            "capacity": 18.0,


        }
        #token = Token.objects.get(user__username='testuser')
        #self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EnergyResource.objects.count(), 1)
        self.assertEqual(
            EnergyResource.objects.get().resource_type, 'wind farm')
        self.assertEqual(EnergyResource.objects.get().status, 'active')
        self.assertEqual(EnergyResource.objects.get().location.json, pnt.json)
        self.assertEqual(EnergyResource.objects.get().capacity, 18.0)
        self.assertEqual(
            EnergyResource.objects.get().owner.username, 'testuser')
