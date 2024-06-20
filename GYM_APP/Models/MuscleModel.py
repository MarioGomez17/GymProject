from django.db import models


class MuscleModel(models.Model):
    Id_MuscleModel = models.AutoField(primary_key=True, db_column='Id_Muscle', default=1)
    Name_MuscleModel = models.CharField(max_length=50, db_column='Name_Muscle', default='')

    class Meta:
        managed = True
        db_table = 'Muscle'