from django.contrib import admin
# from django.contrib.auth.models import Group, User

from .models import Media

# admin.site.unregister(User)
# admin.site.unregister(Group)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass
