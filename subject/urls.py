from django.urls import path
from .views import SubjectApiView
app_name = 'subject'

urlpatterns = [
    path("subjects/", SubjectApiView.as_view(), name="subjects"),
]