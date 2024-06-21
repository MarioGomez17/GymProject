from rest_framework import serializers
from ..Models import SplitUserModel


class SplitUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitUserModel
        fields = '__all__'