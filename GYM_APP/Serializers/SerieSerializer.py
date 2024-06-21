from rest_framework import serializers
from ..Models import SerieModel


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieModel
        fields = '__all__'