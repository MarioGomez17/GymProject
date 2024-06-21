from rest_framework import serializers
from ..Models import GenderModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderModel
        fields = '__all__'
