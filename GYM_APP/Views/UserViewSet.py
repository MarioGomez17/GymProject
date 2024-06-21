from rest_framework import viewsets
from ..Models import UserModel
from ..Serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
