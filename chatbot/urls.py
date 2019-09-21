from django.conf.urls import url
from django.urls import path, re_path
from chatbot.views import ChatterBotApiView, ChatterBotAppView,chat,room


app_name='chatbot'
urlpatterns = [
    #path('chat',ChatterBotAppView.as_view() , name='main'),
    path('chat/',chat , name='chat'),
    re_path(r'^chat/(?P<room_name>[^/]+)/$', room, name='room'),
   # path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]
