from django.urls import path

from school.apps import SchoolConfig

from school.views import LessonsCreateAPIView, LessonsListAPIView, LessonsRetrieveAPIView, LessonsUpdateAPIView, \
    LessonsDestroyAPIView, CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, \
    CourseDestroyAPIView, TestsListAPIView, TestsRetrieveAPIView, QuestionsAPIView

app_name = SchoolConfig.name

urlpatterns = [
    # Lessons
    path('lessons/create/', LessonsCreateAPIView.as_view(), name='lessons-create'),
    path('lessons/', LessonsListAPIView.as_view(), name='lessons-list'),
    path('lessons/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='lessons-detail'),
    path('lessons/update/<int:pk>/', LessonsUpdateAPIView.as_view(), name='lessons-update'),
    path('lessons/delete/<int:pk>/', LessonsDestroyAPIView.as_view(), name='lessons-delete'),

    # Course
    path('course/create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course-detail'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course-update'),
    path('course/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course-delete'),

    # Tests
    path('tests/', TestsListAPIView.as_view(), name='tests-list'),
    path('tests/<int:pk>/', TestsRetrieveAPIView.as_view(), name='test'),
    path('tests/answer/', QuestionsAPIView.as_view(), name='test-answer'),
]
