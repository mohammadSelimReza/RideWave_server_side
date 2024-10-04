from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TravelRequestModel
        fields = "__all__"
class TravelDetailsSerealizer(serializers.ModelSerializer):
    class Meta:
        model = models.TravelDetailsModel
        fields = "__all__"
class TravelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TravelHistoryModel
        fields = "__all__"