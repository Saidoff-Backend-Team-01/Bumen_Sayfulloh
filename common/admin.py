from django.contrib import admin
from .models import Media

@admin.register(MEDIA)
class MediaAdmin(admin.ModelAdmin):
    # list_display = ('type', 'file')
    pass

