from rest_framework import serializers
from ..Models import RoutineTemplateModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineTemplateModel
        fields = '__all__'