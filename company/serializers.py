from rest_framework import serializers
from .models import FAQ, AppInfo, Contacts, ContactWithUs, PrivacyPolicy, SocialMedia, Sponsor


class ContactUsWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = ("name", "phone_number", "message")

    def create(self, validated_data):
        return ContactWithUs.objects.create(**validated_data)


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ("address", "phone_number", "email", "location")


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("question", "answer")
        # exlude = ("id",)


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("telegram", "facebook", "instagram", "linkedin")


class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo
        fields = ("id", "title", "description")


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ("text",)


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ("image", "url")
