import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import chat.routing  # import your chat routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # normal HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})
