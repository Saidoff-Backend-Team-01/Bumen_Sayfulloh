from rest_framework.generics import ListAPIView

from .models import Group, User, UserMessage
from .serializers import GroupSerializer, UserMessageSerializer, UserSerializer


class ProfileApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupApiView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileMessageApiView(ListAPIView):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
