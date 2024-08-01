from rest_framework.generics import ListAPIView
from .models import Subject
from .serializers import SubjectSerializer


class SubjectApiView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer