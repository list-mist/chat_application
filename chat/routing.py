from django.urls import re_path
from . import consumers
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoom.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.NotificationConsumer.as_asgi()),
]
