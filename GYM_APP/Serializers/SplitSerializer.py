from rest_framework import serializers
from ..Models import SplitModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitModel
        fields = '__all__'