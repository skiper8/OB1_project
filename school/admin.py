from django.contrib import admin

from school.models import Course, Lessons, Tests, Questions, Answers


@admin.register(Course)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'description')
    search_fields = ('title',)
    list_filter = ('course',)


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'description')
    search_fields = ('course',)
    list_filter = ('course',)


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'question')
    search_fields = ('test',)
    list_filter = ('test',)


@admin.register(Answers)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_filter = ('id',)
