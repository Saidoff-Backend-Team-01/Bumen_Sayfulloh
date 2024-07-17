from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import News, NewsImange
from .serializers import NewsListSerializer, NewsImangeSerializer


class NewsListView(ListAPIView):
    queryset = News.published.all()
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return self.queryset.order_by("-created_at")
    
    
class NewsImageView(ListAPIView):
    queryset = NewsImange.objects.all()
    serializer_class = NewsImangeSerializer
    
    def get_queryset(self):
        return self.queryset.filter(news=self.kwargs["news_id"])
    
    