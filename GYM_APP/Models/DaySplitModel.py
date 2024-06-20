from django.db import models
from .SplitModel import SplitModel

class DaySplitModel(models.Model):
    Id_DaySplitModel = models.AutoField(primary_key=True, db_column='Id_DaySplit', default=1)
    Name_DaySplitModel = models.CharField(max_length=50, db_column='Name_DaySplit', default='')
    Split_DaySplitModel = models.ForeignKey(SplitModel, on_delete=models.PROTECT, db_column='Split_DaySplit')

    class Meta:
        managed = True
        db_table = 'Day_Split'