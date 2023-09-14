from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from school.models import Course, Lessons
from users.models import User
from rest_framework.test import APITestCase, APIClient


class CourseTestCase(APITestCase):
    """Тесты модели Course"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@yandex.ru',
            first_name='Test',
            last_name='Test',
            is_staff=True,
            is_superuser=False
        )

        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.url_course = '/course/'

    def test_create_course(self):
        """Тест создания модели Course"""
        data = {
            'title': 'course_test',
            'description': 'test test'
        }
        response = self.client.post(f'{self.url_course}create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_course(self):
        """Тест деталей модели Course"""
        self.test_create_course()
        response = self.client.get(f'{self.url_course}2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 2, 'lesson_count': 0, 'lessons': [], 'title': 'course_test', 'image': None,
                          'description': 'test test'})

    def test_list_course(self):
        """Тест листа модели Course"""
        self.test_create_course()
        response = self.client.get(self.url_course)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'count': 1, 'next': None, 'previous': None, 'results': [
                             {'id': 3, 'lesson_count': 0, 'lessons': [], 'title': 'course_test', 'image': None,
                              'description': 'test test'}]}
                         )

class LessonsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@yandex.ru',
            first_name='Test',
            last_name='Test',
            is_staff=True,
            is_superuser=False
        )

        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.url_lessons = '/lessons/'
        self.url_course = '/course/'

    def test_create_lessons(self):
        """Тест создания модели Lessons"""

        data = {
            'title': 'course_test',
            'description': 'test test'
        }
        response_course = self.client.post(f'{self.url_course}create/', data=data)

        response_lessons = self.client.post(f'{self.url_lessons}create/',
                                            {'course': 4, 'title': 'lessons_test', 'description': 'test test',
                                             'link': 'youtube.com'})
        self.assertEqual(response_lessons.status_code, status.HTTP_201_CREATED)
        response_lessons_valid_link = self.client.post(f'{self.url_lessons}create/',
                                                       {'course': 4, 'title': 'lessons_test',
                                                        'description': 'test test', 'link': 'rutube.com'})
        self.assertEqual(response_lessons_valid_link.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_lessons(self):
        """Тест detail модели Lessons"""
        data = {
            'title': 'course_test',
            'description': 'test test'
        }
        response_course = self.client.post(f'{self.url_course}create/', data=data)

        response_lessons = self.client.post(f'{self.url_lessons}create/',
                                            {'course': 5, 'title': 'lessons_test', 'description': 'test test',
                                             'link': 'youtube.com'})
        response = self.client.get(f'{self.url_lessons}2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 2, 'title': 'lessons_test', 'image': None, 'description': 'test test',
                          'link': 'youtube.com', 'course': 5})
