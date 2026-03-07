# dashboard/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sockets/', consumers.MyConsumer.as_asgi()),
]
