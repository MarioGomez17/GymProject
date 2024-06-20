from django.db import models
from .ExerciseModel import ExerciseModel
from .MuscleModel import MuscleModel

class ExerciseVariantModel(models.Model):
    Id_ExerciseVariantModel = models.AutoField(primary_key=True, db_column='Id_ExerciseVariant', default=1)
    Name_ExerciseVariantModel = models.CharField(max_length=100, db_column='Name_ExerciseVariant', default='')
    Exercise_ExerciseVariantModel = models.ForeignKey(ExerciseModel, on_delete=models.PROTECT, db_column='Exercise_ExerciseVariant')
    Muscle_ExerciseVariantModel = models.ForeignKey(MuscleModel, on_delete=models.PROTECT, db_column='Muscle_ExerciseVariant')

    class Meta:
        managed = True
        db_table = 'Exercise_Variant'