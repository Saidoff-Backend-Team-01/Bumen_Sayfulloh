from django.urls import path
from common.views import MediaView
app_name = 'common'

urlpatterns = [
    path('media/', MediaView.as_view(), name='media'),
]