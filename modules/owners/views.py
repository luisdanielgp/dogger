from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Owner
from .serializers import OwnerModelSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ListOwner(APIView): # por convención, ListOwner lista a todos los owners
    '''
    Este endpoint trae todos los owners
    '''

    def get(self, request):
            owners = Owner.objects.all()
            serializer = OwnerModelSerializer(owners, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OwnerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAuthenticated,)


class DetailOwner(APIView):  # por convención detail modifica un owner específico

    def _get_owner(self, id):
        try:
            owner = Owner.objects.get(id=id)
            return owner
        except Owner.DoesNotExist:
            raise Http404

    def get(self, request, id):
        owner = self._get_owner(id)
        serializer = OwnerModelSerializer(owner)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        owner = self._get_owner(id)
        serializer = OwnerModelSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        owner = self._get_owner(id)
        serializer = OwnerModelSerializer(
            owner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        owner = self._get_owner(id)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAuthenticated,)
