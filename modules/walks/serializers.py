from rest_framework import serializers
from .models import Walk

class WalkModelSerializer(serializers.ModelSerializer):

    class Meta:
      model = Walk
      fields = ('__all__')
