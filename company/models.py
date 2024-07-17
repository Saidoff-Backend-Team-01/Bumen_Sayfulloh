from django.db import models
from .validators import phone_number_validator, validate_instagram_url, validate_telegram_url
from common.models import Media
from django.utils.translation import gettext_lazy as _


class Contacts(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, validators=[phone_number_validator])
    email = models.EmailField()
    location = models.URLField()

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _("Contacts")
        
    def __str__(self):
        return self.address


class SocialMedia(models.Model):
    telegram = models.URLField(validators=[validate_telegram_url])
    facebook = models.URLField(validators=[])
    instagram = models.URLField(validators=[validate_instagram_url])
    linkedin = models.URLField(validators=[])

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Medias")

class AppInfo(models.Model):
    title = models.CharField(_('title'), max_length=255)
    desc = models.TextField(_('description'))
    
    class Meta:
        verbose_name = _("AppInfo")
        verbose_name_plural = _("AppInfos")
    
    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.CharField(_('question'), max_length=255)
    answer = models.CharField(_('answerbigint'), max_length=255)
    
    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        
    def __str__(self) -> str:
        return self.question
        
class PrivacyPolicy(models.Model):
    text = models.TextField(_('text'))
    
    class Meta:
        verbose_name = _("Privacy Policy")
        verbose_name_plural = _("Privacy Policies")
        
    def __str__(self):
        return self.text
    
class Sponsor(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    url = models.URLField(_('url'))
    
    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")
        
    def __str__(self):
        return self.url
    
class ContactUs(models.Model):
    name = models.CharField(_('name'), max_length=255)
    phone_number = models.CharField(_('phone_number'), max_length=10)
    message = models.TextField(_('message'))
    
    class Meta:
        verbose_name = _("Contact With Us")
        verbose_name_plural = _("Contact With Us")
        
    def __str__(self) -> str:
        return self.name