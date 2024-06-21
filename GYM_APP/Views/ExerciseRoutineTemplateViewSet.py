from rest_framework import viewsets
from ..Models import ExerciseRoutineTemplateModel
from ..Serializers import ExerciseRoutineTemplateSerializer

class ExerciseRoutineTemplateViewSet(viewsets.ModelViewSet):
    queryset = ExerciseRoutineTemplateModel.objects.all()
    serializer_class = ExerciseRoutineTemplateSerializer