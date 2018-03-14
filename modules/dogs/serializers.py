from rest_framework import serializers
from .models import Dog
from modules.owners.serializers import OwnerModelSerializer

class DogModelSerializer(serializers.ModelSerializer):

  class Meta:
      model = Dog
      fields = ('__all__')

class DogOwnerSerializer(serializers.ModelSerializer):

    owner = OwnerModelSerializer(read_only=True)

    class Meta:
        model = Dog
        fields = ('__all__')
