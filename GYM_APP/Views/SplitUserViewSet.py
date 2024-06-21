from rest_framework import viewsets
from ..Models import SplitUserModel
from ..Serializers import SplitUserSerializer

class SplitUserViewSet(viewsets.ModelViewSet):
    queryset = SplitUserModel.objects.all()
    serializer_class = SplitUserSerializer
