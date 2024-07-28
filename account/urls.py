from django.urls import path

from account import views

app_name = "account"

urlpatterns = [
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
    path("group/", views.GroupApiView.as_view(), name="group"),
    path(
        "profile_message/",
        views.ProfileMessageApiView.as_view(),
        name="profile_message",
    ),
]
