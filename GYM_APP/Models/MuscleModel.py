from django.db import models


class MuscleModel(models.Model):
    Id_Muscle = models.AutoField(primary_key=True, db_column='Id_Muscle', default=1)
    Name_Muscle = models.CharField(max_length=50, db_column='Name_Muscle', default='')

    class Meta:
        managed = True
        db_table = 'Muscle'