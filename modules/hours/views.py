from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Hour
from .serializers import HourModelSerializer
from django.http import Http404


# Create your views here.


class ListHour(APIView): # por convención, ListHour lista a todos los hours
    '''
    Este endpoint trae todos los hours
    '''

    def get(self, request):
            hours = Hour.objects.all()
            serializer = HourModelSerializer(hours, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailHour(APIView):  # por convención detail modifica un hour específico

    def _get_hour(self, id):
        try:
            hour = Hour.objects.get(id=id)
            return hour
        except Hour.DoesNotExist:
            raise Http404

    def get(self, request, id):
        hour = self._get_hour(id)
        serializer = HourModelSerializer(hour)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        hour = self._get_hour(id)
        serializer = HourModelSerializer(hour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        hour = self._get_hour(id)
        serializer = HourModelSerializer(
            hour, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        hour = self._get_hour(id)
        hour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
