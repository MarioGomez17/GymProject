from rest_framework import viewsets
from ..Models import MuscleDayModel
from ..Serializers import MuscleDaySerializer

class MuscleDayViewSet(viewsets.ModelViewSet):
    queryset = MuscleDayModel.objects.all()
    serializer_class = MuscleDaySerializer
