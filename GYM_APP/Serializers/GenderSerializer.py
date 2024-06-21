from rest_framework import serializers
from ..Models import GenderModel


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderModel
        fields = '__all__'
