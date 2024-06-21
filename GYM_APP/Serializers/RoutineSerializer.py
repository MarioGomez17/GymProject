from rest_framework import serializers
from ..Models import RoutineModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineModel
        fields = '__all__'