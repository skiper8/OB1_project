from rest_framework.exceptions import ValidationError


class LinkValidator:
    """Ограничение на модель Lessons не позволяющее вставлять ссылки не из источника youtube.com"""

    def __init__(self, field):
        self.fields = field

    def __call__(self, value):
        reg = 'youtube.com'
        tmp_val = dict(value).get(self.fields)
        if reg not in tmp_val:
            raise ValidationError('Нельзя использовать ссылки не с источника youtube.com')
