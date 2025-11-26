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

    return render(request, "Telefono/confirm_delete.html", {"telefono": tel})

# ---------- Proveedor ----------
def Proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, "Proveedor/detail.html", {"proveedor": proveedor})

@require_http_methods(["GET", "POST"])
def Proveedor_new(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        formCo = CorreoProveedorForm(request.POST)
        formTel = TelefonoProveedorForm(request.POST)
        if form.is_valid() and formCo.is_valid() and formTel.is_valid():
            proveedor = form.save()
            correo = formCo.save(commit=False)
            correo.proveedor = proveedor
            correo.save()
            telefono = formTel.save(commit=False)
            telefono.proveedor = proveedor
            telefono.save()
            return redirect("core:Proveedor_detail", pk=proveedor.pk)
    else:
        form = ProveedorForm()
        formCo = CorreoProveedorForm()
        formTel = TelefonoProveedorForm()
    return render(request,"Proveedor/form.html",{"form": form,"formCo": formCo,"formTel": formTel,"mode": "create",})


@require_http_methods(["GET", "POST"])
def Proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save()
            return redirect("core:Proveedor_detail", pk=proveedor.pk)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, "Proveedor/form.html", {"form": form, "mode": "edit", "proveedor": proveedor})

@require_http_methods(["GET", "POST"])
def Proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        proveedor.delete()
        return redirect("core:home")
    return render(request, "Proveedor/confirm_delete.html", {"proveedor": proveedor})

# ---------- CorreoProveedor ----------
@require_http_methods(["GET", "POST"])
def CorreoProveedor_new(request, proveedor_pk):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_pk)
    if request.method == "POST":
        form = CorreoProveedorForm(request.POST)
        if form.is_valid():
            correo = form.save(commit=False)
            correo.proveedor = proveedor
            correo.save()
            return redirect("core:Proveedor_detail", pk=proveedor.pk)
    else:
        form = CorreoProveedorForm()
    return render(request, "Proveedor/Correo/form.html", {"form": form, "proveedor": proveedor, "mode": "create"},)

@require_http_methods(["GET", "POST"])
def CorreoProveedor_update(request, pk):
    correo = get_object_or_404(CorreoProveedor, pk=pk)
    proveedor = correo.proveedor
    if request.method == "POST":
        form = CorreoProveedorForm(request.POST, instance=correo)
        if form.is_valid():
            form.save()
            return redirect("core:Proveedor_detail", pk=proveedor.pk)
    else:
        form = CorreoProveedorForm(instance=correo)
    return render(request, "Proveedor/Correo/form.html", {"form": form, "proveedor": proveedor, "mode": "edit", "correo": correo},)

@require_http_methods(["GET", "POST"])
def CorreoProveedor_delete(request, pk):
    correo = get_object_or_404(CorreoProveedor, pk=pk)
    proveedor = correo.proveedor
    if request.method == "POST":
        correo.delete()
        return redirect("core:Proveedor_detail", pk=proveedor.pk)
    return render(request,"Proveedor/Correo/confirm_delete.html",{"correo": correo, "proveedor": proveedor},)

# ---------- TelefonoProveedor ----------
@require_http_methods(["GET", "POST"])
def TelefonoProveedor_new(request, proveedor_pk):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_pk)
    if request.method == "POST":
        form = TelefonoProveedorForm(request.POST)
        if form.is_valid():
            tel = form.save(commit=False)
            tel.proveedor = proveedor
            tel.save()
            return redirect("core:Proveedor_detail", pk=proveedor_pk)
    else:
        form = TelefonoProveedorForm()
    return render(request, "Proveedor/Telefono/form.html", {"form": form,"proveedor": proveedor,"mode": "create"})

@require_http_methods(["GET", "POST"])
def TelefonoProveedor_update(request, pk):
    telefono = get_object_or_404(TelefonoProveedor, pk=pk)
    if request.method == "POST":
        form = TelefonoProveedorForm(request.POST, instance=telefono)
        if form.is_valid():
            form.save()
            return redirect("core:Proveedor_detail", pk=telefono.proveedor.pk)
    else:
        form = TelefonoProveedorForm(instance=telefono)
    return render(request, "Proveedor/Telefono/form.html", {"form": form,"telefono": telefono,"mode": "edit"})

@require_http_methods(["GET", "POST"])
def TelefonoProveedor_delete(request, pk):
    tel = get_object_or_404(TelefonoProveedor, pk=pk)
    if request.method == "POST":
        prov_id = tel.proveedor.pk
        tel.delete()
        return redirect("core:Proveedor_detail", pk=prov_id)
    return render(request, "Proveedor/Telefono/confirm_delete.html", {"telefono": tel})








