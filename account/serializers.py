from rest_framework import serializers

from .models import Group, User, UserMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "birth_date", "photo")
