from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserModelSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated



# Create your views here.


class ListUser(APIView): # por convención, ListUser lista a todos los users
    '''
    Este endpoint trae todos los users
    '''

    def get(self, request):
            users = User.objects.all()
            serializer = UserModelSerializer(users, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAuthenticated,)


class DetailUser(APIView):  # por convención detail modifica un user específico

    def _get_user(self, id):
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self._get_user(id)
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = self._get_user(id)
        serializer = UserModelSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        user = self._get_user(id)
        serializer = UserModelSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = self._get_user(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAuthenticated,)
