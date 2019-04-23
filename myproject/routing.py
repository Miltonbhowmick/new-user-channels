from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from accounts.consumers import NewUserConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
    	URLRouter(
    		[
    			path("new-user/", NewUserConsumer),
    		]
    	)
    )
})


