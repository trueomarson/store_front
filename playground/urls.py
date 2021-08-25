from django.urls import path
from . import views

#URLConf - Configuracja
urlpatterns = [
    path("hello/", views.say_hello)
]
