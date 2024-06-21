from rest_framework import serializers
from ..Models import DaySplitModel


class DaySplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaySplitModel
        fields = '__all__'
