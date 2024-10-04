from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,generics
from .serializers import UserSerializer,UserPasswordUpdateSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserPasswordUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserPasswordUpdateSerializer
    queryset = User.objects.all()
    def get_object(self):
        return self.request.user