from rest_framework import serializers
from .models import Gemeinden

class GemeindenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gemeinden
        fields = ('land', 'gemeindekey','gemeinde','gewerbesteuer')