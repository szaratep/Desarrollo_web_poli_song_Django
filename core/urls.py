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
    # ---------- recopilación ----------
    path("Recopilacion/<int:pk>/", views.Recopilacion_detail, name="Recopilacion_detail"),
    path("Recopilacion/new/", views.Recopilacion_New, name="Recopilacion_new"),
    path("Recopilacion/<int:pk>/edit/", views.Recopilacion_update, name="Recopilacion_update"),
    path("Recopilacion/<int:pk>/delete/", views.Recopilacion_delete, name="Recopilacion_delete"),

    # ---------- recopilación-cancion ----------
    path("RecopilacionCancion/<int:pk>/", views.RecopilacionCancion_detail, name="RecopilacionCancion_detail"),
    path("RecopilacionCancion/new/", views.RecopilacionCancion_New, name="RecopilacionCancion_new"),
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

    # ---------- Cancion ----------
    path('canciones/', views.lista_canciones, name='lista_canciones'),
    path('canciones/crear/', views.crear_cancion, name='crear_cancion'),
    path('canciones/editar/<int:id>/', views.editar_cancion, name='editar_cancion'),
    path('canciones/eliminar/<int:id>/', views.eliminar_cancion, name='eliminar_cancion'),

    # ---------- Vinilo ----------
    path('vinilos/', views.lista_vinilos, name='lista_vinilos'),
    path('vinilos/crear/', views.crear_vinilo, name='crear_vinilo'),
    path('vinilos/editar/<int:id>/', views.editar_vinilo, name='editar_vinilo'),
    path('vinilos/eliminar/<int:id>/', views.eliminar_vinilo, name='eliminar_vinilo'),

    # ---------- ViniloCancion ----------
    path('vinilo-cancion/', views.lista_vinilo_cancion, name='lista_vinilo_cancion'),
    path('vinilo-cancion/crear/', views.crear_vinilo_cancion, name='crear_vinilo_cancion'),
    path('vinilo-cancion/eliminar/<int:id>/', views.eliminar_vinilo_cancion, name='eliminar_vinilo_cancion'),
]