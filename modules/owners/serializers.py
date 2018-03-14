from rest_framework import serializers
from .models import Owner
from modules.dogs.serializers import DogModelSerializer

class OwnerModelSerializer(serializers.ModelSerializer):

  class Meta:
      model = Owner
      fields = ('__all__')

class OwnerDogsSerializer(serializers.ModelSerializer):

    dogs = DogModelSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('__all__')
