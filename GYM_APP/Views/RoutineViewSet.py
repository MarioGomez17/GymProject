from rest_framework import viewsets
from ..Models import RoutineModel
from ..Serializers import RoutineSerializer

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = RoutineModel.objects.all()
    serializer_class = RoutineSerializer
