from django.db import models
from .ExerciseVariantModel import ExerciseVariantModel
from .RoutineTemplateModel import RoutineTemplateModel

class ExerciseRoutineTemplateModel(models.Model):
    Id_ExerciseRoutineTemplateModel = models.AutoField(primary_key=True, db_column='Id_ExerciseRoutineTemplate', default=1)
    Series_ExerciseRoutineTemplateModel = models.IntegerField(db_column='Series_ExerciseRoutineTemplate', default=0)
    ExerciseVariant_ExerciseRoutineTemplateModel = models.ForeignKey(ExerciseVariantModel, on_delete=models.PROTECT, db_column='ExerciseVariant_ExerciseRoutineTemplate')
    RoutineTemplate_ExerciseRoutineTemplateModel = models.ForeignKey(RoutineTemplateModel, on_delete=models.PROTECT, db_column='RoutineTemplate_ExerciseRoutineTemplate')

    class Meta:
        managed = True
        db_table = 'Exercise_Routine_Template'