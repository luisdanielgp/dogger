from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Dog
from .serializers import DogModelSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ListDog(APIView): # por convención, ListDog lista a todos los dogs
    '''
    Este endpoint trae todos los dogs
    '''

    def get(self, request):
            dogs = Dog.objects.all()
            serializer = DogModelSerializer(dogs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DogModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAuthenticated,)


class DetailDog(APIView):  # por convención detail modifica un dog específico

    def _get_dog(self, id):
        try:
            dog = Dog.objects.get(id=id)
            return dog
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, id):
        dog = self._get_dog(id)
        serializer = DogModelSerializer(dog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        dog = self._get_dog(id)
        serializer = DogModelSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        dog = self._get_dog(id)
        serializer = DogModelSerializer(
            dog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        dog = self._get_dog(id)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAuthenticated,)
