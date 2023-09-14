from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    page_size = 10


class LessonsPaginator(PageNumberPagination):
    page_size = 10
