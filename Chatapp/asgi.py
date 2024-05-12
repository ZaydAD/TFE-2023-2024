# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
import Chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chatapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Chatapp.routing.websocket_urlpatterns  # Make sure this import and reference are correct
        )
    ),
})
