from rest_framework import viewsets
from ..Models import DaySplitModel
from ..Serializers import DaySplitSerializer

class DaySplitViewSet(viewsets.ModelViewSet):
    queryset = DaySplitModel.objects.all()
    serializer_class = DaySplitSerializer