from rest_framework import viewsets
from ..Models import ExerciseVariantModel
from ..Serializers import ExerciseVariantSerializer

class ExerciseVariantViewSet(viewsets.ModelViewSet):
    queryset = ExerciseVariantModel.objects.all()
    serializer_class = ExerciseVariantSerializer
