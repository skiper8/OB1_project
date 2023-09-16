from rest_framework import status
from rest_framework.test import APITestCase


class UsersTestCase(APITestCase):
    """Тесты модели Course"""

    def setUp(self):
        self.url_users = '/users/'

    def test_create_users(self):
        """Тест создания модели User"""
        data = {
            'email': 'testuser@yandex.ru',
            'password': 'test456'
        }
        response = self.client.post(f'{self.url_users}create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
