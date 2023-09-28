from rest_framework.exceptions import ValidationError
import re


class PhoneValidator:
    """Ограничение на модель User не для поля phone"""

    def __init__(self, field):
        self.fields = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.fields)
        result = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[9]0-{2}$',
                          tmp_val)
        if bool(result) is False:
            raise ValidationError('Неверный формат номера телефона')


class EmailValidator:
    """Ограничение на модель User не для поля email"""

    def __init__(self, field):
        self.fields = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.fields)
        result = re.match(r'^[а-яА-Яa-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$',
                          tmp_val)
        if bool(result) is False:
            raise ValidationError('Неверный формат email')

        if len(tmp_val) < 10:
            raise ValidationError('Длинна email не может быть меньше 5 символов')


