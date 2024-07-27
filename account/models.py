from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import Media
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return self.username
    
    
class Group(models.Model):
    name = models.CharField(_('name'), max_length=255)
    users = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        
    def __str__(self):
        return self.name
    
    
class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(_('message'))
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = 'User Message'
        verbose_name_plural = 'User Messages'
        
    def __str__(self):
        return self.user