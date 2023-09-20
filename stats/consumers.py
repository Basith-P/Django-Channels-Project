import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DashboardConsumer(AsyncWebsocketConsumer):
    # This method is called when a WebSocket connection is established.
    async def connect(self):
        # Get the 'dashboard_slug' from the URL route's keyword arguments.
        dashboard_slug = self.scope["url_route"]["kwargs"]["dashboard_slug"]
        self.dashboard_slug = dashboard_slug
        await self.accept()

    # This method is called when a WebSocket connection is closed.
    async def disconnect(self, close_code):
        print(f"disconnected with code: {close_code}")

    # This method is called when the server receives a message from a client.
    async def receive(self, text_data):
        # Parse the received JSON message into Python objects.
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]

        # Print the received message and sender for debugging purposes.
        print(f"received message: {message} from {sender}")

        # Send a response message back to the client.
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender
        }))
