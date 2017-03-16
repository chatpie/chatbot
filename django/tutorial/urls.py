from django.conf.urls import url, include
from tutorial.quickstart import views

urlpatterns = [
    url(r'^keyboard', views.keyboard),
    url(r'^message', views.message),
    url(r'^friend', views.friend),
    url(r'^chat_room', views.chat_room),
]
