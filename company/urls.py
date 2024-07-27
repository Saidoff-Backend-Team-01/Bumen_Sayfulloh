from django.urls import path
from .views import *
app_name = 'company'

urlpatterns = [
    path("contactus/", ContactUsWebView.as_view(), name="contact_with_us"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("faqs/", FaqApiView.as_view(), name="faqs"),
    path("socialmedia/", SocialMediaView.as_view(), name="socialmedia"),
    path("appinfo/", AppInfoView.as_view(), name="appinfo"),
    path("privacypolicy/", PrivacyPolicyView.as_view(), name="privacypolicy"),
    path("sponsor/", SponsorView.as_view(), name="sponsor"),
]