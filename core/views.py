from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import *
from .forms import *
# Create your views here.

def home(reuqest):
    return render(reuqest, "home.html", {"title": "polisong"})

# ---------- Usuario ----------

def User_detail(request, pk):
    obj = get_object_or_404(Usuario, pk=pk)
    return render(request, "Usuario/detail.html",{"Usuario": obj})

@require_http_methods(["GET", "POST"])
def User_New(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        formCo = CorreoForm(request.POST)
        formtel= TelefonoForm(request.POST)
        if form.is_valid() and formCo.is_valid() and formtel.is_valid():
            us = form.save()
            
            co = formCo.save(commit=False)
            co.usuario = us
            co.save()

            tel = formtel.save(commit=False)
            tel.usuario = us
            tel.save()
            return redirect("core:User_detail", pk=us.pk)
    else:
        form = UsuarioForm()
        formCo = CorreoForm()
        formtel= TelefonoForm()
    return render(request, "Usuario/form.html", {"form": form, "formCo": formCo, "formtel": formtel, "mode": "create"})

@require_http_methods(["GET","POST"])
def User_update(request, pk):
    obj = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        formUs = UsuarioForm(request.POST, instance=obj)
        if formUs.is_valid():
            obj = formUs.save()
            return redirect("core:User_detail", pk=obj.pk)
    else:
        formUs = UsuarioForm(instance=obj)
    return render(request, "Usuario/form.html", {"form": formUs, "mode": "edit", "usuario": obj})

@require_http_methods(["GET", "POST"])
def User_delete(request, pk):
    obj = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("core:home")
    return render(request, "Usuario/confirm_delete.html", {"Usuario": obj})

# ---------- Correo ----------
@require_http_methods(["GET", "POST"])
def Correo_new(request, user_pk):
    usuario = get_object_or_404(Usuario, pk=user_pk)
    if request.method == "POST":
        form = CorreoForm(request.POST)
        if form.is_valid():
            correo = form.save(commit=False)
            correo.usuario = usuario
            correo.save()
            return redirect("core:User_detail", pk=usuario.pk)
    else:
        form = CorreoForm()
    return render(request, "Correo/form.html", {"form": form,"usuario": usuario,"mode": "create",})

@require_http_methods(["GET", "POST"])
def Correo_update(request, pk):
    correo = get_object_or_404(Correo, pk=pk)

    if request.method == "POST":
        form = CorreoForm(request.POST, instance=correo)
        if form.is_valid():
            form.save()
            return redirect("core:User_detail", pk=correo.usuario.pk)
    else:
        form = CorreoForm(instance=correo)

    return render(request, "Correo/form.html", {"form": form,"correo": correo,"mode": "edit",})

@require_http_methods(["GET", "POST"])
def Correo_delete(request, pk):
    correo = get_object_or_404(Correo, pk=pk)
    if request.method == "POST":
        usuario = correo.usuario.pk
        correo.delete()
        return redirect("core:User_detail", pk=usuario)
    return render(request, "Correo/confirm_delete.html", {"correo": correo})

# ---------- Telefono ----------
@require_http_methods(["GET", "POST"])
def Telefono_new(request, user_pk):
    usuario = get_object_or_404(Usuario, pk=user_pk)
    if request.method == "POST":
        form = TelefonoForm(request.POST)
        if form.is_valid():
            tel = form.save(commit=False)
            tel.usuario = usuario
            tel.save()
            return redirect("core:User_detail", pk=usuario.pk)
    else:
        form = TelefonoForm()
    return render(request, "Telefono/form.html", {"form": form,"usuario": usuario,"mode": "create"})

@require_http_methods(["GET", "POST"])
def Telefono_update(request, pk):
    telefono = get_object_or_404(Telefono, pk=pk)
    if request.method == "POST":
        form = TelefonoForm(request.POST, instance=telefono)
        if form.is_valid():
            form.save()
            return redirect("core:User_detail", pk=telefono.usuario.pk)
    else:
        form = TelefonoForm(instance=telefono)
    return render(request, "Telefono/form.html", {"form": form,"telefono": telefono,"mode": "edit"})

@require_http_methods(["GET", "POST"])
def Telefono_delete(request, pk):
    tel = get_object_or_404(Telefono, pk=pk)

    if request.method == "POST":
        user_id = tel.usuario.pk
        tel.delete()
        return redirect("core:User_detail", pk=user_id)

    return render(request, "Telefono/confirm_delete.html", {
        "telefono": tel
    })


