from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework import status,views
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response

#

class UserRequestView(viewsets.ModelViewSet):
    queryset = models.TravelRequestModel.objects.all()
    serializer_class = serializers.UserRequestSerializer
    permission_classes = [AllowAny]

class TravelDetailsView(viewsets.ModelViewSet):
    queryset = models.TravelDetailsModel.objects.all()
    serializer_class = serializers.TravelDetailsSerealizer
    permission_classes = [AllowAny]

class TravelHistoryView(viewsets.ModelViewSet):
    queryset = models.TravelHistoryModel.objects.all()
    serializer_class = serializers.TravelHistorySerializer
    permission_classes = [AllowAny]


class EndRideView(views.APIView):
    def post(self, request, request_no):
        try:
            # Get the ongoing travel details using request_no
            travel_details = models.TravelDetailsModel.objects.get(request_no=request_no, travel_running=True)

            # Call the method to end the ride and transfer to history
            travel_details.end_ride()

            return Response({'message': 'Ride ended successfully!'}, status=status.HTTP_200_OK)
        
        except models.TravelDetailsModel.DoesNotExist:
            return Response({'error': 'Ride not found or already ended!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    