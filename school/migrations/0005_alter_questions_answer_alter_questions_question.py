# Generated by Django 4.2.5 on 2023-09-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_course_title_alter_lessons_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='ответ на вопрос'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='вопрос'),
        ),
    ]
