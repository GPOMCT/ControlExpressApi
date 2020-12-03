from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter
from apps.chat.consumers import ChatConsumer
from apps.mqtt.consumers import MqttConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
    'channel': ChannelNameRouter(
        {
            "mqtt": MqttConsumer
        }
    )
})