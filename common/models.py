from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from .validators import file_validator

class Media(models.Model):
    
    class MediaType(models.TextChoices):
        IMAGE = 'image', _('image')
        VIDEO = 'video', _('video')
        AUDIO = 'audio', _('audio')
        FILE = 'file', _('file')
        MUSIC = 'music', _('music')
        
    type = models.CharField(_('type'), max_length=50, choices=MediaType.choices)
    file = models.FileField(_('file'), upload_to='media/', validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'png', 'jpeg', 'gif', 'mp4', 'mp3']
    ), file_validator])