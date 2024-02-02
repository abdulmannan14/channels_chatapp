from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Chat(models.Model):
    content = models.CharField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
