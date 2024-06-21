from rest_framework import viewsets
from ..Models import GenderModel
from ..Serializers import GenderSerializer

class GenderViewSet(viewsets.ModelViewSet):
    queryset = GenderModel.objects.all()
    serializer_class = GenderSerializer
