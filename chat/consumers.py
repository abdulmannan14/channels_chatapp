import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from . import models as chat_models


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("entering=====")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.user_id = self.scope['user'].id
        # addding==============
        room = await database_sync_to_async(chat_models.ChatRoom.objects.get)(name=self.room_name)
        chat = chat_models.Chat(content=message, user=self.scope['user'], chatroom=room)
        # chat.save()
        await database_sync_to_async(chat.save)()
        # =====================
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user_id
            })

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
