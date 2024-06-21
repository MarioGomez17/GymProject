from django.db import models


class ExerciseModel(models.Model):
    Id_ExerciseModel = models.AutoField(primary_key=True, db_column='Id_Exercise')
    Name_ExerciseModel = models.CharField(max_length=100, db_column='Name_Exercise', default='')

    class Meta:
        managed = True
        db_table = 'Exercise'