from django.urls import path

from .views import NewsImageView, NewsListView

app_name = "news"

urlpatterns = [
    path("", NewsListView.as_view(), name="news_list"),
    path("newsimage/", NewsImageView.as_view(), name="newsimage"),
]
