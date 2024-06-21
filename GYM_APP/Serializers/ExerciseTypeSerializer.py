from rest_framework import serializers
from ..Models import ExerciseTypeModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseTypeModel
        fields = '__all__'
