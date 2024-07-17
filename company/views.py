from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from yaml import serialize
from company.models import ContactUs, FAQ, Contacts, Sponsor, PrivacyPolicy, AppInfo, SocialMedia
from company.serializers import ContactWithUsSerializer, FAQSerializer, ContactsSerializer, SocialMediaSerializer, AppInfoSerializer, PrivacyPolicySerializer, SponsorSerializer


class ContactWithUsView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactWithUsSerializer
    

class ContactView(CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    
    
class FAQAPIView(APIView):
    serializer_class = FAQSerializer
    def get(self, request, *args, **kwargs):
        try:
            queryset = FAQ.objects.all()
            serializer = FAQSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(data={"message": "Something went wrong."}, status=500)
      
        
class SocialMediaView(CreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    
    
class AppInfoView(CreateAPIView):
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer
    
    
class PrivacyPolicyView(CreateAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
    
    
class SponsorView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer