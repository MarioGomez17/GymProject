from rest_framework import serializers
from ..Models import RoutineTemplateModel


class RoutineTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineTemplateModel
        fields = '__all__'