from django.shortcuts import render
from rest_framework import generics
from .models import Dog
from .serializers import DogModelSerializer, DogOwnerSerializer

# Create your views here.

class ListGenericDog(generics.ListCreateAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogOwnerSerializer

class DetailGenericDog(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogModelSerializer
