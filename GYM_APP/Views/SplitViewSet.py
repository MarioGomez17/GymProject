from rest_framework import viewsets
from ..Models import SplitModel
from ..Serializers import SplitSerializer

class SplitViewSet(viewsets.ModelViewSet):
    queryset = SplitModel.objects.all()
    serializer_class = SplitSerializer
