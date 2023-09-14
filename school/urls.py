from django.urls import path

from school.apps import SchoolConfig

from school.views import *

app_name = SchoolConfig.name

urlpatterns = [
    # Lessons
    path('lessons/create/', LessonsCreateView.as_view(), name='lessons-create'),
    path('lessons/', LessonsListView.as_view(), name='lessons-list'),
    path('lessons/<int:pk>/', LessonsDetailView.as_view(), name='lessons-delete'),
    path('lessons/update/<int:pk>/', LessonsUpdateView.as_view(), name='lessons-update'),
    path('lessons/delete/<int:pk>/', LessonsDeleteView.as_view(), name='lessons-delete'),

    # Course
    path('course/create/', CourseCreateView.as_view(), name='course-create'),
    path('course/', CourseListView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-delete'),
    path('course/update/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('course/delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),

    # Tests
    path('tests/', TestsAPIView.as_view(), name='tests-list'),
    path('tests/test/', QuestionsAPIView.as_view(), name='test-1'),
]
