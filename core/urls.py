from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.home, name="home"),
    path("catalogo/", views.catalogo, name="catalogo"),
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
    # ---------- recopilación ----------
    path("Recopilacion/<int:pk>/", views.Recopilacion_detail, name="Recopilacion_detail"),
    path("Recopilacion/new/", views.Recopilacion_New, name="Recopilacion_new"),
    path("Recopilacion/<int:pk>/edit/", views.Recopilacion_update, name="Recopilacion_update"),
    path("Recopilacion/<int:pk>/delete/", views.Recopilacion_delete, name="Recopilacion_delete"),

    # ---------- recopilación-cancion ----------
    path("RecopilacionCancion/<int:pk>/", views.RecopilacionCancion_detail, name="RecopilacionCancion_detail"),
    path("RecopilacionCancion/new/<int:recopilacion_pk>/", views.RecopilacionCancion_New, name="RecopilacionCancion_new"),
    path("RecopilacionCancion/<int:pk>/edit/", views.RecopilacionCancion_update, name="RecopilacionCancion_update"),
    path("RecopilacionCancion/<int:pk>/delete/", views.RecopilacionCancion_delete, name="RecopilacionCancion_delete"),

    # ---------- valoración ----------
    path("Valoracion/<int:pk>/", views.Valoracion_detail, name="Valoracion_detail"),
    path("Valoracion/new/", views.Valoracion_New, name="Valoracion_new"),
    path("Valoracion/<int:pk>/edit/", views.Valoracion_update, name="Valoracion_update"),
    path("Valoracion/<int:pk>/delete/", views.Valoracion_delete, name="Valoracion_delete"),


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

    # ----- DiscoMp3 CRUD -----
    path("discmp3/", views.discomp3_list, name="discomp3_list"),
    path("discmp3/new/", views.discomp3_new, name="discomp3_new"),
    path("discmp3/<int:pk>/", views.discomp3_detail, name="discomp3_detail"),
    path("discmp3/<int:pk>/edit/", views.discomp3_update, name="discomp3_update"),
    path("discmp3/<int:pk>/delete/", views.discomp3_delete, name="discomp3_delete"),

    # ----- Canción CRUD -----
    path("cancion/", views.cancion_list, name="cancion_list"),
    path("cancion/new/", views.cancion_new, name="cancion_new"),
    path("cancion/<int:pk>/", views.cancion_detail, name="cancion_detail"),
    path("cancion/<int:pk>/edit/", views.cancion_update, name="cancion_update"),
    path("cancion/<int:pk>/delete/", views.cancion_delete, name="cancion_delete"),

    # ----- Vinilo CRUD -----
    path("vinilo/", views.vinilo_list, name="vinilo_list"),
    path("vinilo/new/", views.vinilo_new, name="vinilo_new"),
    path("vinilo/<int:pk>/", views.vinilo_detail, name="vinilo_detail"),
    path("vinilo/<int:pk>/edit/", views.vinilo_update, name="vinilo_update"),
    path("vinilo/<int:pk>/delete/", views.vinilo_delete, name="vinilo_delete"),

        # ---------- Pedido ----------
    path("pedido/", views.pedido_list, name="pedido_list"),
    path("pedido/new/", views.pedido_new, name="pedido_new"),
    path("pedido/<int:pk>/", views.pedido_detail, name="pedido_detail"),
    path("pedido/<int:pk>/edit/", views.pedido_update, name="pedido_update"),
    path("pedido/<int:pk>/delete/", views.pedido_delete, name="pedido_delete"),


]