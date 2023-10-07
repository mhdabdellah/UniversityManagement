from rest_framework import viewsets
from .models import Faculté, Filière, Etudiant
from .serializers import FacultySerializer, SectorSerializer, StudentSerializer

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculté.objects.all()
    serializer_class = FacultySerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Filière.objects.all()
    serializer_class = SectorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = StudentSerializer
