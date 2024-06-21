from rest_framework import viewsets
from ..Models import ExerciseModel
from ..Serializers import ExerciseSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = ExerciseModel.objects.all()
    serializer_class = ExerciseSerializer
