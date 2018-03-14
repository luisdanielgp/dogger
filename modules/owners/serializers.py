from rest_framework import serializers
from .models import Owner

class OwnerModelSerializer(serializers.ModelSerializer):

  class Meta:
      model = Owner
      fields = ('__all__')
