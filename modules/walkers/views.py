from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Walker
from .serializers import WalkerModelSerializer
from django.http import Http404


# Create your views here.


class ListWalker(APIView): # por convención, ListWalker lista a todos los walkers
    '''
    Este endpoint trae todos los walkers
    '''

    def get(self, request):
            walkers = Walker.objects.all()
            serializer = WalkerModelSerializer(walkers, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WalkerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailWalker(APIView):  # por convención detail modifica un walker específico

    def _get_walker(self, id):
        try:
            walker = Walker.objects.get(id=id)
            return walker
        except Walker.DoesNotExist:
            raise Http404

    def get(self, request, id):
        walker = self._get_walker(id)
        serializer =WalkerModelSerializer(walker)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        Walker = self._get_walker(id)
        serializer = WalkerModelSerializer(walker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        walker = self._get_walker(id)
        serializer = WalkerModelSerializer(
            walker, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        walker = self._get_walker(id)
        walker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
