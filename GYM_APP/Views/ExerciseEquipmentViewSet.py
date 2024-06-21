from rest_framework import viewsets
from ..Models import ExerciseEquipmentModel
from ..Serializers import ExerciseEquipmentSerializer

class ExerciseEquipmentViewSet(viewsets.ModelViewSet):
    queryset = ExerciseEquipmentModel.objects.all()
    serializer_class = ExerciseEquipmentSerializer