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


]