from rest_framework import serializers
from .models import Walker
from modules.hours.serializers import HourModelSerializer

class WalkerModelSerializer(serializers.ModelSerializer):

    hours = HourModelSerializer(many=True, read_only=True)

    class Meta:
      model = Walker
      fields = ('id', 'user', '' 'hours')
