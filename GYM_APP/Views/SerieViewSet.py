from rest_framework import viewsets
from ..Models import SerieModel
from ..Serializers import SerieSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = SerieModel.objects.all()
    serializer_class = SerieSerializer
