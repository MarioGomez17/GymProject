from django.db import models


class SplitModel(models.Model):
    Id_SplitModel = models.AutoField(primary_key=True, db_column='Id_Split')
    Name_SplitModel = models.CharField(max_length=50, db_column='Name_Split', default='')

    class Meta:
        managed = True
        db_table = 'Split'