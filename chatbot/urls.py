from django.conf.urls import url
from django.urls import path
from chatbot import views
from chatbot.views import ChatterBotApiView, ChatterBotAppView


app_name='chatbot'
urlpatterns = [
    path('chat',ChatterBotAppView.as_view() , name='main'),
    path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]
