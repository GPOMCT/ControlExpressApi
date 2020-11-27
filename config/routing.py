from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
# chat/routing.py
from django.urls import re_path

from apps.chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    # 'http':
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
})