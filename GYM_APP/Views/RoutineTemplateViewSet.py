from rest_framework import viewsets
from ..Models import RoutineTemplateModel
from ..Serializers import RoutineTemplateSerializer

class RoutineTemplateViewSet(viewsets.ModelViewSet):
    queryset = RoutineTemplateModel.objects.all()
    serializer_class = RoutineTemplateSerializer
