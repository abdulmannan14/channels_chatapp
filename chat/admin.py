from django.contrib import admin

# Register your models here.
from .models import Chat, ChatRoom

admin.site.register(Chat)
admin.site.register(ChatRoom)
