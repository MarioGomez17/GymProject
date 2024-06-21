from rest_framework import serializers
from ..Models import SplitUserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitUserModel
        fields = '__all__'