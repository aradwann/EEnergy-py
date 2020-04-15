from .models import Article
from django.contrib.auth import get_user_model
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token


class ArticlesModelTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # create a test user
        test_user1 = get_user_model().objects.create_user(
            username="testuser", password="testpassword")
        test_user1.save()

    def test_create_article(self):
        """
        Ensure we can create a new article object.
        """
        url = reverse('articles-list')
        data = {
            "title": "wind farm",
            "body": "active",
            "comments":[]
        }

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.get().title, 'wind farm')
        self.assertEqual(Article.objects.get().body, 'active')
        self.assertEqual(Article.objects.get().author.username, 'testuser')
