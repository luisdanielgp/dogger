from rest_framework import serializers
from .models import Hour

class HourModelSerializer(serializers.ModelSerializer):

  class Meta:
      model = Hour
      fields = ('__all__')
