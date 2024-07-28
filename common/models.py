# from .validators import file_validator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Media(models.Model):

    class MediaType(models.TextChoices):
        IMAGE = "image", _("image")
        VIDEO = "video", _("video")
        AUDIO = "audio", _("audio")
        FILE = "file", _("file")
        MUSIC = "music", _("music")

    type = models.CharField(_("type"), max_length=50, choices=MediaType.choices)
    file = models.FileField(
        _("file"),
        upload_to="media/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "png", "jpeg", "gif", "mp4", "mp3"]
            )
        ],
    )

    def clean(self):
        if self.type not in self.MediaType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.type == self.MediaType.IMAGE:
            if self.file.name.split(".")[-1] not in ["jpg", "jpeg", "png"]:
                raise ValidationError(_("Invalid Image File"))

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Mediaes")
