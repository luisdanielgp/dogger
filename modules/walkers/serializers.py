from rest_framework import serializers
from .models import Walker

class WalkerModelSerializer(serializers.ModelSerializer):

  class Meta:
      model = Walker
      fields = ('__all__')
