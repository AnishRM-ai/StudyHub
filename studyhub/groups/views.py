from rest_framework import viewsets
from .models import StudyGroup
from .serializers import StudyGroupSerializer

class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
