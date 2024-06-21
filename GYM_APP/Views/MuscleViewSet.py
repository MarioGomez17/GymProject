from rest_framework import viewsets
from ..Models import MuscleModel
from ..Serializers import MuscleSerializer

class MuscleViewSet(viewsets.ModelViewSet):
    queryset = MuscleModel.objects.all()
    serializer_class = MuscleSerializer
