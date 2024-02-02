from django.shortcuts import render, redirect

# def chatPage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login-user")
#     context = {}
#     return render(request, "chat/chatPage.html", context)
#


from django.shortcuts import render
from django.views import View
from . import models as chatroom_models


class Index(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login-user")
        return render(request, 'chatrooms/index.html')


class Room(View):
    def get(self, request, room_name):
        room = chatroom_models.ChatRoom.objects.filter(name=room_name).first()
        chats = []
        if room:
            chats = chatroom_models.Chat.objects.filter(chatroom=room)
        else:
            room = chatroom_models.ChatRoom(name=room_name)
            room.save()

        context = {
            'chats': chats,
            'room_name': room_name,
            'username': request.user.username
        }
        return render(request, 'chatrooms/room.html', context)
