from django.contrib import admin

from news.models import News, NewsImange
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']

@admin.register(NewsImange)
class NewsImangeAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'news']
