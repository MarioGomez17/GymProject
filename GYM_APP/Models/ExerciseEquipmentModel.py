from django.db import models


class ExerciseEquipmentModel(models.Model):
    Id_ExerciseEquipmentModel = models.AutoField(primary_key=True, db_column='Id_ExerciseEquipment', default=1)
    Name_ExerciseEquipmentModel = models.CharField(max_length=100, db_column='Name_ExerciseEquipment', default='')

    class Meta:
        managed = True
        db_table = 'Exercise_Equipment'