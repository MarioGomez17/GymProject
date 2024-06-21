from rest_framework import serializers
from ..Models import RoutineModel


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineModel
        fields = '__all__'