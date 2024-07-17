from rest_framework import serializers

from news.models import News, NewsImange
from common.serializers import MediaURlSerializer


class NewsListSerializer(serializers.ModelSerializer):
    image = MediaURlSerializer(read_only=True)

    class Meta:
        model = News
        fields = ("id", "create_at", "title", "description", "image", "is_publish")


class NewsImangeSerializer(serializers.ModelSerializer):
    file = MediaURlSerializer(read_only=True)
    news = MediaURlSerializer(read_only=True)
    
    class Meta:
        model = NewsImange
        fields = ("id", "file", "news")