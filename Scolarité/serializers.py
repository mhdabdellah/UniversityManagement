from rest_framework import serializers
from .models import Faculté, Filière, Etudiant

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculté
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filière
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
