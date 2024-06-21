from rest_framework import viewsets
from ..Models import ExerciseTypeModel
from ..Serializers import ExerciseTypeSerializer

class ExerciseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExerciseTypeModel.objects.all()
    serializer_class = ExerciseTypeSerializer
