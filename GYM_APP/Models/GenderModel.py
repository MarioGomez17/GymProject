from django.db import models


class GenderModel(models.Model):
    Id_GenderModel = models.AutoField(primary_key=True, db_column='Id_Gender')
    Name_GenderModel = models.CharField(max_length=50, db_column='Name_Gender', default='')

    class Meta:
        managed = True
        db_table = 'Gender'