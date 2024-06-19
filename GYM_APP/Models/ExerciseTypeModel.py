from django.db import models


class ExerciseTypeModel(models.Model):
    Id_ExerciseTypeModel = models.AutoField(primary_key=True, db_column='Id_ExerciseType', default=1)
    Name_ExerciseTypeModel = models.CharField(max_length=100, db_column='Name_ExerciseType', default='')

    class Meta:
        managed = True
        db_table = 'Exercise_Type'