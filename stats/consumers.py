import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("connected")

        # await self.channel_layer.group_add(
        #     "dashboard",
        #     self.channel_name
        # )

    async def disconnect(self, close_code):
        # await self.channel_layer.group_discard(
        #     "dashboard",
        #     self.channel_name
        # )
        print(f"disconnected with code: {close_code}")

    async def stats_update(self, event):
        await self.send_json(event)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]

        print(f"received message: {message} from {sender}")

        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender
        }))
