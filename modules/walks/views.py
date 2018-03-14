from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Walk
from .serializers import WalkModelSerializer
from django.http import Http404


# Create your views here.


class ListWalk(APIView): # por convención, ListWalk lista a todos los walks
    '''
    Este endpoint trae todos los walks
    '''

    def get(self, request):
            walks = Walk.objects.all()
            serializer = WalkModelSerializer(walks, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WalkModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailWalk(APIView):  # por convención detail modifica un walk específico

    def _get_walk(self, id):
        try:
            walk = Walk.objects.get(id=id)
            return walk
        except Walk.DoesNotExist:
            raise Http404

    def get(self, request, id):
        walk = self._get_walk(id)
        serializer = WalkModelSerializer(walk)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        walk = self._get_walk(id)
        serializer = WalkModelSerializer(walk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        walk = self._get_walk(id)
        serializer = WalkModelSerializer(
            walk, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        walk = self._get_walk(id)
        walk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
