from rest_framework import serializers
from ..Models import ExerciseModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = '__all__'
