from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.home, name="home"),
    path("api/ping/", views.api_ping, name="api_ping"),
    path('api/echo/', views.api_echo, name="api_echo"),
]