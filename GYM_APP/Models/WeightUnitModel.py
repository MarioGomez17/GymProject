from django.db import models

class WeightUnitModel(models.Model):
    Id_WeightUnitModel = models.AutoField(primary_key=True, db_column='Id_WeightUnit', default=1)
    Name_WeightUnitModel = models.CharField(max_length=50, db_column='Name_WeightUnit', default='')
    Symbol_WeightUnitModel = models.CharField(max_length=10, db_column='Symbol_WeightUnit', default='')

    class Meta:
        managed = True
        db_table = 'WeightUnit'