from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Media

from .managers import NewsManager


class News(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"))
    create_at = models.DateTimeField(_("create_at"), auto_now_add=True)
    is_publish = models.BooleanField(_("is_publish"), default=True)
    published = NewsManager()

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
