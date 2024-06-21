from rest_framework import serializers
from ..Models import MuscleModel


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleModel
        fields = '__all__'