import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # make sure this points to your chat app's routing.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')  # replace myproject with your project name

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # handles normal HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
