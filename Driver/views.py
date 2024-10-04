from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework import status
from rest_framework.permissions import AllowAny
# 
from rest_framework.response import Response


class UserView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]
# Create your views here.
class DriverView(viewsets.ModelViewSet):
    queryset = models.DriverUserModel.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [AllowAny]

class DriverRegistrationView(viewsets.ModelViewSet):
    queryset = models.DriverUserModel.objects.all()
    serializer_class = serializers.DriverRegistrationSerializer
    permission_classes = [AllowAny]
    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)