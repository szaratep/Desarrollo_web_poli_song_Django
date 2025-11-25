from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.home, name="home"),

    # ---------- Usuario ----------
    path('usuario/new/', views.User_New, name = 'User_New'),
    path('usuario/<int:pk>/', views.User_detail, name = 'User_detail'),
    path('usuario/<int:pk>/edit/', views.User_update, name = 'User_update'),
    path('usuario/<int:pk>/delete/', views.User_delete, name = 'User_delete'),

    # ---------- Correo ----------
    path("Correo/new/<int:user_pk>/", views.Correo_new, name="Correo_new"),
    path("Correo/<str:pk>/edit/", views.Correo_update, name="Correo_update"),
    path("Correo/<str:pk>/delete/", views.Correo_delete, name="Correo_delete"),

    # ---------- telefono ----------
    path("Telefono/new/<int:user_pk>/", views.Telefono_new, name="Telefono_new"),
    path("Telefono/<str:pk>/edit/", views.Telefono_update, name="Telefono_update"),
    path("Telefono/<str:pk>/delete/", views.Telefono_delete, name="Telefono_delete"),


]