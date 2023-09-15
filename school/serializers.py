from rest_framework import serializers

from school.models import Course, Lessons, Tests, Questions, Answers
from school.validators import LinkValidator


class LessonsSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Lessons """

    class Meta:
        model = Lessons
        fields = '__all__'
        validators = [LinkValidator(field='link')]


class CourseSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Course """

    lesson_count = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True, source='lessons_set')

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return Lessons.objects.filter(course=obj).count()


class QuestionsSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Questions """

    class Meta:
        model = Questions
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Answers """

    class Meta:
        model = Answers
        fields = '__all__'


class TestsSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Tests """

    class Meta:
        model = Tests
        fields = '__all__'
