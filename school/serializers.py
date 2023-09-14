from rest_framework import serializers

from school.models import Course, Lessons, Tests, Questions
from school.validators import LinkValidator


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
        validators = [LinkValidator(field='link')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True, source='lessons_set')

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return Lessons.objects.filter(course=obj).count()


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
