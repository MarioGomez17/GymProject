from rest_framework import serializers
from ..Models import ExerciseVariantModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseVariantModel
        fields = '__all__'
