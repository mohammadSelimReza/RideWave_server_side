import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RideRequestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("ride_requests", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("ride_requests", self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to the group
        await self.channel_layer.group_send(
            "ride_requests",
            {
                'type': 'ride_request',
                'message': message
            }
        )

    # Handle an event sent to the group
    async def ride_request(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
