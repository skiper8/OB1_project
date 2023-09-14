from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@yandex.ru',
            first_name='User',
            last_name='User',
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        user.set_password('zazaza456852')
        user.save()
