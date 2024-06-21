from rest_framework import serializers
from ..Models import ExerciseEquipmentModel


class ExerciseEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseEquipmentModel
        fields = '__all__'
