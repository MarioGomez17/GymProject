from django.db import models
from .WeightUnitModel import WeightUnitModel
from .UserModel import UserModel
from .MuscleDayModel import MuscleDayModel


class RoutineModel(models.Model):
    Id_RoutineModel = models.AutoField(primary_key=True, db_column='Id_Routine')
    Name_RoutineModel = models.CharField(max_length=50, db_column='Name_Routine', default='')
    Date_RoutineModel = models.DateTimeField(auto_now_add=True, db_column='Date_Routine')
    Focus_RoutineModel = models.TextField(db_column='Focus_Routine', default='')
    Exercises_RoutineModel = models.IntegerField(db_column='Exercises_Routine', default=0)
    Series_RoutineModel = models.IntegerField(db_column='Series_Routine', default=0)
    Weight_RoutineModel = models.FloatField(db_column='Weight_Routine', default=0)
    WeightUnit_RoutineModel = models.ForeignKey(WeightUnitModel, on_delete=models.PROTECT, db_column='WeightUnit_Routine')
    User_RoutineModel = models.ForeignKey(UserModel, on_delete=models.PROTECT, db_column='User_Routine')
    MuscleDay_RoutineModel = models.ForeignKey(MuscleDayModel, on_delete=models.PROTECT, db_column='MuscleDay_Routine')

    class Meta:
        managed = True
        db_table = 'Routine'