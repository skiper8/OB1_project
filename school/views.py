from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from school.models import Course, Lessons, Tests, Questions, Answers
from school.paginators import CoursePaginator, LessonsPaginator
from school.permissions import IsStaff
from school.serializers import CourseSerializer, LessonsSerializer, TestsSerializer, QuestionsSerializer

""" CRUD для моделей Course, Lessons, Tests, Questions, Answers """


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsStaff]


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator
    permission_classes = [IsAuthenticated]


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsStaff]


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsStaff]


class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsStaff]


class LessonsCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer
    permission_classes = [IsStaff]


class LessonsListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    pagination_class = LessonsPaginator
    permission_classes = [IsAuthenticated]


class LessonsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsStaff]


class LessonsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsStaff]


class LessonsDestroyAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
    permission_classes = [IsStaff]


class TestsListAPIView(generics.ListAPIView):
    serializer_class = TestsSerializer
    queryset = Tests.objects.all()
    permission_classes = [IsAuthenticated]


class TestsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:
        answers = [Answers.answer for Answers in Answers.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].lower()
        user_answer = request.data.get('user_answer')
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct}, )


class QuestionsAPIView(APIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        question = [Questions.question for Questions in Questions.objects.all()]
        return Response({'questions': question}, )

    def post(self, request, *args, **kwargs):
        answer = [Answers.answer for Answers in Answers.objects.all()]
        user_answer = request.data.get('user_answer')

        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})
