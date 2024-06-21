from django.db import models
from .WeightUnitModel import WeightUnitModel
from .GenderModel import GenderModel


class UserModel(models.Model):
    Id_UserModel = models.AutoField(primary_key=True, db_column='Id_User')
    Name_UserModel = models.CharField(max_length=50, db_column='Name_User', default='')
    LastName_UserModel = models.CharField(max_length=50, db_column='LastName_User', default='')
    Email_UserModel = models.CharField(max_length=50, db_column='Email_User', default='')
    Password_UserModel = models.CharField(max_length=50, db_column='Password_User', default='')
    Age_UserModel = models.IntegerField(db_column='Age_User', default=0)
    Weight_UserModel = models.FloatField(db_column='Weight_User', default=0)
    WeightUnit_UserModel = models.ForeignKey(WeightUnitModel, on_delete=models.PROTECT, db_column='WeightUnit_User')
    Gender_UserModel = models.ForeignKey(GenderModel, on_delete=models.PROTECT, db_column='Gender_User')

    class Meta:
        managed = True
        db_table = 'User'
