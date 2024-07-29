from django.urls import path

from account import views

app_name = "account"

urlpatterns = [
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
]
