from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import User, Group, UserMessage
from .serializers import UserSerializer, GroupSerializer, UserMessageSerializer


class ProfileApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class GroupApiView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    
class ProfileMessageApiView(ListAPIView):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer