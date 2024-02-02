from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path("", chat_views.chatPage, name="chat-page"),
    path("login", LoginView.as_view(template_name="chatrooms/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('', chat_views.Index.as_view(), name='chat-page'),
    path('<str:room_name>/', chat_views.Room.as_view(), name='room'),
]
