from django.db import models
from .SplitModel import SplitModel

class RoutineTemplateModel(models.Model):
    Id_RoutineTemplateModel = models.AutoField(primary_key=True, db_column='Id_RoutineTemplate', default=1)
    Name_RoutineTemplateModel = models.CharField(max_length=100, db_column='Name_RoutineTemplate', default='')
    Focus_RoutineTemplateModel = models.TextField(db_column='Focus_RoutineTemplate', default='')
    Exercises_RoutineTemplateModel = models.IntegerField(db_column='Exercises_RoutineTemplate', default=0)
    Series_RoutineTemplateModel = models.IntegerField(db_column='Series_RoutineTemplate', default=0)
    Split_RoutineTemplateModel = models.ForeignKey(SplitModel, on_delete=models.PROTECT, db_column='Split_RoutineTemplate')

    class Meta:
        managed = True
        db_table = 'Routine_Template'