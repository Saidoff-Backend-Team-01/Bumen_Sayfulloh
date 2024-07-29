from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class ProfileApiView(APIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            seralizer = UserSerializer(User.objects.all(), many=True)
            return Response(seralizer.data, status=200)

        except Exception:
            return Response(data={"message": "Internal Server Error"}, status=500)
