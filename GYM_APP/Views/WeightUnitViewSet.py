from rest_framework import viewsets
from ..Models import WeightUnitModel
from ..Serializers import WeightUnitSerializer

class WeightUnitViewSet(viewsets.ModelViewSet):
    queryset = WeightUnitModel.objects.all()
    serializer_class = WeightUnitSerializer
