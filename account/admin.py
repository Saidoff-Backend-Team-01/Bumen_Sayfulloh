from django.contrib import admin
from django.utils.html import format_html

from .models import Group, User, UserMessage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display_fields = ["first_name", "last_name", "birth_date", "show_image"]
    list_filter = ["first_name", "birth_date"]
    search_fields = ["first_name"]

    def show_image(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50px" />'.format(obj.image.url))
        return "No Image"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display_fields = ["name", "users"]
    list_filter = ["name", "users"]
    search_fields = ["name"]


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display_fields = ["user", "message", "show_image", "group"]
    list_filter = ["user", "group"]
    search_fields = ["user"]

    def show_image(self, obj):
        if obj.file:
            return format_html('<img src="{}" width="50px" />'.format(obj.image.url))
        return "No Image"
