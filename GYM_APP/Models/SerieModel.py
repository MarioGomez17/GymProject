from django.db import models
from .ExerciseVariantModel import ExerciseVariantModel
from .ExerciseTypeModel import ExerciseTypeModel
from .ExerciseEquipmentModel import ExerciseEquipmentModel
from .WeightUnitModel import WeightUnitModel
from .RoutineModel import RoutineModel

class SerieModel(models.Model):
    Id_SerieModel = models.AutoField(primary_key=True, db_column='Id_Serie')
    Name_SerieModel = models.CharField(max_length=50, db_column='Name_Serie', default='')
    ExerciseVariant_SerieModel = models.ForeignKey(ExerciseVariantModel, on_delete=models.PROTECT, db_column='ExerciseVariant_Serie')
    ExerciseType_SerieModel = models.ForeignKey(ExerciseTypeModel, on_delete=models.PROTECT, db_column='ExerciseType_Serie')
    ExerciseEquipment_SerieModel = models.ForeignKey(ExerciseEquipmentModel, on_delete=models.PROTECT, db_column='ExerciseEquipment_Serie')
    Weight_SerieModel = models.FloatField(db_column='Weight_Serie', default=0)
    WeightUnit_SerieModel = models.ForeignKey(WeightUnitModel, on_delete=models.PROTECT, db_column='WeightUnit_Serie')
    Rest_SerieModel = models.FloatField(db_column='Rest_Serie', default=0)
    Routine_SerieModel = models.ForeignKey(RoutineModel, on_delete=models.PROTECT, db_column='Routine_Serie')

    class Meta:
        managed = True
        db_table = 'Serie'