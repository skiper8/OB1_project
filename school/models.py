from django.db import models

NULLABLE: dict[str, bool] = {'blank': True, 'null': True}


class Course(models.Model):
    """ Модель курса """

    title = models.CharField(max_length=50, verbose_name='название курса', **NULLABLE)
    image = models.ImageField(upload_to='course_image/', verbose_name='изображение для курса', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'Курс {self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('title',)


class Lessons(models.Model):
    """ Модель лекций """

    title = models.CharField(max_length=50, verbose_name='название лекции', **NULLABLE)
    image = models.ImageField(upload_to='lessons_image/', verbose_name='изображение для лекции', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link = models.CharField(max_length=500, verbose_name='ссылка', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

    def __str__(self):
        return f'Лекция {self.title} по курсу {self.course}'

    class Meta:
        verbose_name = 'лекция'
        verbose_name_plural = 'лекции'
        ordering = ('course',)


class Tests(models.Model):
    """ Модель тестов для курсов """

    course = models.ForeignKey(Course, verbose_name='по какой лекции тест', on_delete=models.CASCADE, **NULLABLE)
    description = models.TextField(verbose_name='описание теста', **NULLABLE)

    def __str__(self):
        return f'Тест по курсу {self.course}'

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        ordering = ('course',)


class Questions(models.Model):
    """ Модель вопросов к тестам """

    test = models.ForeignKey(Tests, verbose_name='по какой лекции тест', on_delete=models.CASCADE, **NULLABLE)
    question = models.CharField(max_length=50, verbose_name='вопрос', **NULLABLE)

    def __str__(self):
        return f'Вопрос {self.question}'

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        ordering = ('test',)


class Answers(models.Model):
    """ Модель ответов к вопросам """

    question = models.ForeignKey(Questions, verbose_name='Вопрос', on_delete=models.CASCADE, **NULLABLE)
    answer = models.CharField(max_length=40, verbose_name='ответ на вопрос', **NULLABLE)

    def __str__(self):
        return f'Ответ на вопрос {self.question}'

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
