from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from ..models import EnergyResource
from ..serializers import EnergyResourceSerializer
from django.contrib.gis.geos import Point

ENERGY_RESOURCES_LIST_URL = reverse('energy-resource-list')


def detail_url(resource_id):
    """return resource detail url"""
    return reverse('energy-resource-detail',
                   args=[resource_id])


def sample_resource(owner, *args):
    """Create a sample resourc and return it
    takes only the owner and resource type arguments"""
    resource = EnergyResource.objects.create(
        resource_type="wind farm",
        status="active",
        location=Point(*args),
        capacity=18.0,
        consumption=12.0,
        net_energy=6.0,
        owner=owner
    )
    return resource


class EnergyResourcePublicAPITests(TestCase):
    """Tests for the Public API"""

    def setUp(self):
        self.client = APIClient()

    def test_get_energy_resources_list_with_unauthenticated_user(self):
        """
        test getting a list of energy resources object view
        with unauthenticated user
        """
        self.client.logout()
        response = self.client.get(ENERGY_RESOURCES_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_energy_resource_with_unauthenticated_user(self):
        """
        Ensure we can create a new energy_resource
        object with a valid payload and unauthenticated user
        """

        payload = {"resource_type": "wind farm",
                   "status": "active",
                   "location": Point(2, 3).json,
                   "capacity": 18.0,
                   "consumption": 12.0,
                   }
        response = self.client.post(
            ENERGY_RESOURCES_LIST_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class EnergyResourcePrivateAPITests(TestCase):
    """
    Test case for creating an energy resource
    object through the used view
    """

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_energy_resource_with_valid_payload(self):
        """
        Ensure we can create a new energy_resource
        object with a valid payload and authenticated user
        """

        payload = {"resource_type": "wind farm",
                   "status": "active",
                   "location": Point(3, 5).json,
                   "capacity": 18.0,
                   "consumption": 12.0,
                   }

        response = self.client.post(
            ENERGY_RESOURCES_LIST_URL, payload, format='json')
        resource = EnergyResource.objects.filter(
            owner=self.user, location=payload['location'])
        exists = resource.exists()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_create_energy_resource_with_invalid_payload(self):
        """
        Ensure we can create a new energy_resource
        object with invalid payload and authenticated user
        """

        payload = {
            "status": "active",
            "location": Point(6, 5).json,
            "capacity": 18.0,
            "consumption": 12.0,
        }

        response = self.client.post(
            ENERGY_RESOURCES_LIST_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_energy_resource_list(self):
        """
        test getting a list of energy resources object
        with authenticated user
        """
        test_user2 = get_user_model().objects.create_user(
            username="testuser2", password="testpassword")
        sample_resource(test_user2, 2, 5)
        sample_resource(test_user2, 3, 5)

        response = self.client.get(ENERGY_RESOURCES_LIST_URL)
        resources = EnergyResource.objects.all()
        serializer = EnergyResourceSerializer(resources, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_partial_update_resource_with_owner(self):
        """
        Test partial update using patch method
        with an authenticated user and resource owner
        """
        resource = sample_resource(self.user, 5, 4)

        payload = {
            'resource_type': 'PV'
        }

        url = detail_url(resource.id)
        self.client.patch(url, payload)

        resource.refresh_from_db()
        self.assertEqual(resource.resource_type, payload['resource_type'])

    def test_partial_update_resource_with_non_owner(self):
        """
        Test partial update using patch method
        with an authenticated user but not the owner
        """
        test_user2 = get_user_model().objects.create_user(
            username="testuser2", password="testpassword")
        resource = sample_resource(test_user2, 5, 4)

        payload = {
            'resource_type': 'PV'
        }

        url = detail_url(resource.id)
        response = self.client.patch(url, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_full_update_resource(self):
        """
        Test full update using put method
        with an authenticated user and resource owner
        """
        resource = sample_resource(self.user, 5, 6)

        payload = {
            "resource_type": "hydro",
            "status": "active",
            "location": Point(6, 5).json,
            "capacity": 18.0,
            "consumption": 12.0,
        }
        url = detail_url(resource.id)
        self.client.put(url, payload)

        resource.refresh_from_db()
        self.assertEqual(resource.resource_type, payload['resource_type'])
        self.assertEqual(resource.status, payload['status'])
        self.assertEqual(resource.location.json, payload['location'])
