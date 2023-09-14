import requests
from django.views import generic
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from school.models import Course, Lessons, Tests, Questions
from school.paginators import CoursePaginator, LessonsPaginator
from school.serializers import CourseSerializer, LessonsSerializer, TestsSerializer, QuestionsSerializer


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseSerializer


class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator


class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseUpdateView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()


class LessonsCreateView(generics.CreateAPIView):
    serializer_class = LessonsSerializer


class LessonsListView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    pagination_class = LessonsPaginator


class LessonsDetailView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsUpdateView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsDeleteView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()


class TestsAPIView(generics.ListAPIView):
    serializer_class = TestsSerializer
    queryset = Tests.objects.all()


class QuestionsAPIView(APIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()

    def get(self, request):
        question = [Questions.question for Questions in Questions.objects.all()]
        return Response(question)

    def post(self, *args, **kwargs):
        answer = [Questions.answer for Questions in Questions.objects.all()]
        user_answer = requests.post('answer')

        if answer == user_answer:
            return Response('Верно!', status.HTTP_200_OK)
        else:
            return Response('Неверно!', status.HTTP_200_OK)
