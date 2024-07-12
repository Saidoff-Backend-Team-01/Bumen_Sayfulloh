from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def file_validator(value):
    if not value.endswith('png'):
        raise ValidationError(_('Only .png files are allowed.'))