from django.db import models
from .SplitModel import SplitModel
from .UserModel import UserModel


class SplitUserModel(models.Model):
    Id_SplitUserModel = models.AutoField(primary_key=True, db_column='Id_SplitUser', default=1)
    Split_SplitUserModel = models.ForeignKey(SplitModel, on_delete=models.PROTECT, db_column='Split_SplitUser')
    User_SplitUserModel = models.ForeignKey(UserModel, on_delete=models.PROTECT, db_column='User_SplitUser')

    class Meta:
        managed = True
        db_table = 'Split_User'
