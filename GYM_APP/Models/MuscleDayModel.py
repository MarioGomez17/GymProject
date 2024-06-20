from django.db import models
from .MuscleModel import MuscleModel
from .DaySplitModel import DaySplitModel


class MuscleDayModel(models.Model):
    Id_MuscleDayModel = models.AutoField(primary_key=True, db_column='Id_MuscleDay', default=1)
    Muscle_MuscleDayModel = models.ForeignKey(MuscleModel, on_delete=models.PROTECT, db_column='Muscle_MuscleDay')
    Day_MuscleDayModel = models.ForeignKey(DaySplitModel, on_delete=models.PROTECT, db_column='Day_MuscleDay')

    class Meta:
        managed = True
        db_table = 'Muscle_Day'
