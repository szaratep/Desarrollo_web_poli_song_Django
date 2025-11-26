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
    path("Correo/<int:pk>/edit/", views.Correo_update, name="Correo_update"),
    path("Correo/<int:pk>/delete/", views.Correo_delete, name="Correo_delete"),

    # ---------- telefono ----------
    path("Telefono/new/<int:user_pk>/", views.Telefono_new, name="Telefono_new"),
    path("Telefono/<int:pk>/edit/", views.Telefono_update, name="Telefono_update"),
    path("Telefono/<int:pk>/delete/", views.Telefono_delete, name="Telefono_delete"),

    # ---------- Proveedor ----------
    path("Proveedor/new/", views.Proveedor_new, name="Proveedor_new"),
    path("Proveedor/<int:pk>/", views.Proveedor_detail, name="Proveedor_detail"),
    path("Proveedor/<int:pk>/edit/", views.Proveedor_update, name="Proveedor_update"),
    path("Proveedor/<int:pk>/delete/", views.Proveedor_delete, name="Proveedor_delete"),

    # ---------- Correo Proveedor ----------
    path("Proveedor/Correo/new/<int:proveedor_pk>/", views.CorreoProveedor_new, name="CorreoProveedor_new"),
    path("Proveedor/Correo/<int:pk>/edit/", views.CorreoProveedor_update, name="CorreoProveedor_update"),
    path("Proveedor/Correo/<int:pk>/delete/", views.CorreoProveedor_delete, name="CorreoProveedor_delete"),

    # ---------- Telefono Proveedor ----------
    path("Proveedor/Telefono/new/<int:proveedor_pk>/", views.TelefonoProveedor_new, name="TelefonoProveedor_new"),
    path("Proveedor/Telefono/<int:pk>/edit/", views.TelefonoProveedor_update, name="TelefonoProveedor_update"),
    path("Proveedor/Telefono/<int:pk>/delete/", views.TelefonoProveedor_delete, name="TelefonoProveedor_delete"),
]