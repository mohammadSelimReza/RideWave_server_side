from django.urls import re_path
from .consumers import RideRequestConsumer

websocket_urlpatterns = [
    re_path(r'ws/ride/requests/$', RideRequestConsumer.as_asgi()),
]
