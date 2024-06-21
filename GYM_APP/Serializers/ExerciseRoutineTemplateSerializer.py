from rest_framework import serializers
from ..Models import ExerciseRoutineTemplateModel


class ExerciseRoutineTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseRoutineTemplateModel
        fields = '__all__'
