from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subject
from .serializers import SubjectSerializer


class SubjectApiView(APIView):
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        try:
            seralizer = SubjectSerializer(Subject.objects.all(), many=True)
            return Response(seralizer.data, status=200)
        except Exception:
            return Response(data={"message": "Internal Server Error"}, status=500)