from django.core.exceptions import ValidationError
from django.utils import timezone

now = timezone.now()


def date_validator(value):
    if value < now:
        raise ValidationError(
            ('%(value)s is not a correcrt year!'),
            params={'value': value},
        )
