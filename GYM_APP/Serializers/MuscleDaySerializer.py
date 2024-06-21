from rest_framework import serializers
from ..Models import MuscleDayModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleDayModel
        fields = '__all__'