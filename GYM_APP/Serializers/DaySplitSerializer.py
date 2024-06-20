from rest_framework import serializers
from ..Models import DaySplitModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaySplitModel
        fields = '__all__'
