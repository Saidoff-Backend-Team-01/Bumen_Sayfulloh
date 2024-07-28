from rest_framework import serializers

from .models import Group, User, UserMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "birth_date", "photo")

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", "users")

    def create(self, validated_data):
        return Group.objects.create(**validated_data)


class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ("user", "message", "file", "group")

    def create(self, validated_data):
        return UserMessage.objects.create(**validated_data)
