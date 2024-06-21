from rest_framework import serializers
from ..Models import WeightUnitModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightUnitModel
        fields = '__all__'
