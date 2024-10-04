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
class RiderView(viewsets.ModelViewSet):
    queryset = models.RiderUserModel.objects.all()
    serializer_class = serializers.RiderSerializer
    permission_classes = [AllowAny]

class RiderRegistrationView(viewsets.ModelViewSet):
    queryset = models.RiderUserModel.objects.all()
    serializer_class = serializers.RiderRegistrationSerializer
    permission_classes = [AllowAny]