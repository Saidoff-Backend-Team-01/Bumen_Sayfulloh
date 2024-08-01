from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from company.serializers import (
    AppInfoSerializer,
    ContactsSerializer,
    ContactUsWebSerializer,
    FAQSerializer,
    PrivacyPolicySerializer,
    SocialMediaSerializer,
    SponsorSerializer,
)

from .models import (
    FAQ,
    AppInfo,
    Contacts,
    ContactWithUs,
    PrivacyPolicy,
    SocialMedia,
    Sponsor,
)


class ContactUsWebView(CreateAPIView):
    queryset = ContactWithUs.objects.all()
    serializer_class = ContactUsWebSerializer


class ContactView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class FaqApiView(APIView):
    serializer_class = FAQSerializer

    def get(self, request, *args, **kwargs):
        try:
            seralizer = FAQSerializer(FAQ.objects.all(), many=True)
            return Response(seralizer.data, status=200)
        except Exception:
            return Response(data={"message": "Internal Server Error"}, status=500)


class SocialMediaView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class AppInfoView(ListAPIView):
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer


class PrivacyPolicyView(ListAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer


class SponsorView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
