from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = {
            'username': 'testuser',
            'password': 'testpass123'
        }

    def test_register(self):
        response = self.client.post('/api/register/', self.test_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)

    def test_login(self):
        # Create a user first
        User.objects.create_user(**self.test_user)
        # Try to login
        response = self.client.post('/api/login/', self.test_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)