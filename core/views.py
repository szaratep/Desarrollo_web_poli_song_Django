from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse 
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
# ---------- Recopilación ----------

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

# ---------- Cancion ----------
def cancion_list(request):
    canciones = Cancion.objects.all()
    return render(request, "cancion/list.html", {"canciones": canciones})

def cancion_detail(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    return render(request, "cancion/detail.html", {"cancion": cancion})

@require_http_methods(["GET", "POST"])
def cancion_new(request):
    if request.method == "POST":
        form = CancionForm(request.POST)
        if form.is_valid():
            cancion = form.save()
            return redirect("core:cancion_detail", pk=cancion.pk)
    else:
        form = CancionForm()

    return render(request, "cancion/form.html", {"form": form,"mode": "create",})

@require_http_methods(["GET", "POST"])
def cancion_update(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            cancion = form.save()
            return redirect("core:cancion_detail", pk=cancion.pk)
    else:
        form = CancionForm(instance=cancion)
    return render(request, "cancion/form.html", {"form": form,"mode": "edit","cancion": cancion})

@require_http_methods(["GET", "POST"])
def cancion_delete(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        cancion.delete()
        return redirect("core:cancion_list")
    return render(request, "cancion/confirm_delete.html", {"cancion": cancion})

# ---------- Vinilo ----------
def vinilo_list(request):
    qs = Vinilo.objects.all()
    return render(request, "vinilo/list.html", {"vinilos": qs})

def vinilo_detail(request, pk):
    vinilo = get_object_or_404(Vinilo, pk=pk)
    canciones = Cancion.objects.filter(vinilocancion__vinilo=vinilo)

    return render(request, "vinilo/detail.html", {
        "vinilo": vinilo,
        "canciones": canciones
    })

@require_http_methods(["GET", "POST"])
def vinilo_new(request):
    if request.method == "POST":
        form = ViniloForm(request.POST)
        if form.is_valid():
            vinilo = form.save()
            #limpiar relaciones previas (por si acaso)
            ViniloCancion.objects.filter(vinilo=vinilo).delete()
            # guardar nuevas relaciones
            for c in form.cleaned_data["canciones"]:
                ViniloCancion.objects.create(vinilo=vinilo, cancion=c)
            return redirect("core:vinilo_detail", pk=vinilo.pk)
    else:
        form = ViniloForm()
    return render(request, "vinilo/form.html", {"form": form,"mode": "create",})

@require_http_methods(["GET", "POST"])
def vinilo_update(request, pk):
    vinilo = get_object_or_404(Vinilo, pk=pk)
    # obtener canciones asociadas actualmente
    canciones_rel = Cancion.objects.filter(vinilocancion__vinilo=vinilo)
    if request.method == "POST":
        form = ViniloForm(request.POST, instance=vinilo)
        if form.is_valid():
            vinilo = form.save()
            # borrar relaciones anteriores
            ViniloCancion.objects.filter(vinilo=vinilo).delete()
            # crear nuevas relaciones
            for c in form.cleaned_data["canciones"]:
                ViniloCancion.objects.create(vinilo=vinilo, cancion=c)
            return redirect("core:vinilo_detail", pk=vinilo.pk)
    else:
        form = ViniloForm(instance=vinilo)
        form.fields["canciones"].initial = canciones_rel
    return render(request, "vinilo/form.html", {"form": form,"mode": "edit","vinilo": vinilo})

@require_http_methods(["GET", "POST"])
def vinilo_delete(request, pk):
    vinilo = get_object_or_404(Vinilo, pk=pk)
    if request.method == "POST":
        vinilo.delete()
        return redirect("core:vinilo_list")
    return render(request, "vinilo/confirm_delete.html", {"vinilo": vinilo})


# ----------  Discomp3 ----------
def discomp3_list(request):
    qs = DiscoMp3.objects.all()
    return render(request, "discmp3/list.html", {"discos": qs})

def discomp3_detail(request, pk):
    disco = get_object_or_404(DiscoMp3, pk=pk)
    canciones = Cancion.objects.filter(discomp3cancion__disco_mp3=disco)
    return render(request, "discmp3/detail.html", {"disco": disco, "canciones": canciones})

@require_http_methods(["GET", "POST"])
def discomp3_new(request):
    if request.method == "POST":
        form = DiscoMp3Form(request.POST)
        if form.is_valid():
            disco = form.save()
            # limpiar relaciones previas (por si acaso)
            DiscoMp3Cancion.objects.filter(disco_mp3=disco).delete()
            # crear nuevas relaciones
            for c in form.cleaned_data["canciones"]:
                DiscoMp3Cancion.objects.create(disco_mp3=disco, cancion=c)
            return redirect("core:discomp3_detail", pk=disco.pk)
    else:
        form = DiscoMp3Form()
    return render(request, "discmp3/form.html", {"form": form,"mode": "create",})

@require_http_methods(["GET", "POST"])
def discomp3_update(request, pk):
    disco = get_object_or_404(DiscoMp3, pk=pk)
    # Preseleccionar canciones actuales
    canciones_rel = Cancion.objects.filter(discomp3cancion__disco_mp3=disco)
    if request.method == "POST":
        form = DiscoMp3Form(request.POST, instance=disco)
        if form.is_valid():
            disco = form.save()
            # limpiar relaciones previas
            DiscoMp3Cancion.objects.filter(disco_mp3=disco).delete()
            # crear nuevas relaciones
            for c in form.cleaned_data["canciones"]:
                DiscoMp3Cancion.objects.create(disco_mp3=disco, cancion=c)
            return redirect("core:discomp3_detail", pk=disco.pk)
    else:
        form = DiscoMp3Form(instance=disco)
        form.fields["canciones"].initial = canciones_rel
    return render(request, "discmp3/form.html", {"form": form, "mode": "edit", "disco": disco,})

@require_http_methods(["GET", "POST"])
def discomp3_delete(request, pk):
    disco = get_object_or_404(DiscoMp3, pk=pk)
    if request.method == "POST":
        disco.delete()
        return redirect("core:discomp3_list")
    return render(request, "discmp3/confirm_delete.html", {"disco": disco})



def Recopilacion_detail(request, pk):
    obj = get_object_or_404(Recopilacion, pk=pk)
    return render(request, "Recopilacion/detail.html", {"recopilacion": obj})

@require_http_methods(["GET", "POST"])
def Recopilacion_New(request):
    usuario = Usuario.objects.first()  
    if not usuario:
        return HttpResponse("No hay usuarios disponibles para asignar.", status=400)

    if request.method == "POST":
        form = RecopilacionForm(request.POST)
        if form.is_valid():
            recop = form.save(commit=False)
            recop.usuario = usuario
            recop.save()
            return redirect("core:Recopilacion_detail", pk=recop.pk)
    else:
        form = RecopilacionForm(initial={"usuario": usuario})

    return render(
        request,
        "Recopilacion/form.html",
        {"form": form, "mode": "create", "usuario": usuario}
    )
@require_http_methods(["GET", "POST"])
def Recopilacion_update(request, pk):
    obj = get_object_or_404(Recopilacion, pk=pk)

    if request.method == "POST":
        form = RecopilacionForm(request.POST, instance=obj)
        if form.is_valid():
            recop = form.save(commit=False)
            recop.usuario = obj.usuario  # aseguramos que no cambie
            recop.save()
            return redirect("core:Recopilacion_detail", pk=recop.pk)
    else:
        form = RecopilacionForm(instance=obj)

    return render(
        request,
        "Recopilacion/form.html",
        {"form": form, "mode": "edit", "recopilacion": obj}
    )

@require_http_methods(["GET", "POST"])
def Recopilacion_delete(request, pk):
    obj = get_object_or_404(Recopilacion, pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect("core:home")

    return render(
        request,
        "Recopilacion/confirm_delete.html",
        {"recopilacion": obj}
    )
# ---------- RecopilaciónCancion ----------

def RecopilacionCancion_detail(request, pk):
    obj = get_object_or_404(RecopilacionCancion, pk=pk)
    return render(request, "RecopilacionCancion/detail.html", {"rc": obj})

@require_http_methods(["GET", "POST"])
def RecopilacionCancion_New(request):
    usuario = Usuario.objects.first()  
    if not usuario:
        return HttpResponse("No hay usuarios disponibles para asignar.", status=400)
    try:
        recopilacion = Recopilacion.objects.filter(usuario=usuario).first()
    except Recopilacion.DoesNotExist:
        recopilacion = None

    if request.method == "POST":
        form = RecopilacionCancionForm(request.POST)
        if form.is_valid():
            rc = form.save(commit=False)
            # asignar la recopilación automáticamente si no viene del form
            rc.recopilacion = recopilacion
            rc.save()
            return redirect("core:RecopilacionCancion_detail", pk=rc.pk)
    else:
        form = RecopilacionCancionForm(initial={"recopilacion": recopilacion})

    return render(
        request,
        "RecopilacionCancion/form.html",
        {"form": form, "mode": "create", "recopilacion": recopilacion}
    )

@require_http_methods(["GET", "POST"])
def RecopilacionCancion_update(request, pk):
    obj = get_object_or_404(RecopilacionCancion, pk=pk)

    if request.method == "POST":
        form = RecopilacionCancionForm(request.POST, instance=obj)
        if form.is_valid():
            rc = form.save(commit=False)
            rc.recopilacion = obj.recopilacion  # aseguramos que no cambie
            rc.save()
            return redirect("core:RecopilacionCancion_detail", pk=rc.pk)
    else:
        form = RecopilacionCancionForm(instance=obj)

    return render(
        request,
        "RecopilacionCancion/form.html",
        {"form": form, "mode": "edit", "rc": obj}
    )

@require_http_methods(["GET", "POST"])
def RecopilacionCancion_delete(request, pk):
    obj = get_object_or_404(RecopilacionCancion, pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect("core:home")

    return render(
        request,
        "RecopilacionCancion/confirm_delete.html",
        {"rc": obj}
    )

# ---------- Valoracion ----------

def Valoracion_detail(request, pk):
    obj = get_object_or_404(Valoracion, pk=pk)
    return render(request, "Valoracion/detail.html", {"valoracion": obj})

@require_http_methods(["GET", "POST"])
def Valoracion_New(request):
    usuario = Usuario.objects.first()  
    if not usuario:
        return HttpResponse("No hay usuarios disponibles para asignar.", status=400)
    
    pedido = Pedido.objects.filter(usuario=usuario).first()

    if request.method == "POST":
        form = ValoracionForm(request.POST)
        if form.is_valid():
            val = form.save(commit=False)
            val.usuario = usuario
            val.pedido = pedido
            val.save()
            return redirect("core:Valoracion_detail", pk=val.pk)
    else:
        form = ValoracionForm(initial={"usuario": usuario, "pedido": pedido})

    return render(
        request,
        "Valoracion/form.html",
        {"form": form, "mode": "create", "pedido": pedido}
    )

@require_http_methods(["GET", "POST"])
def Valoracion_update(request, pk):
    obj = get_object_or_404(Valoracion, pk=pk)

    if request.method == "POST":
        form = ValoracionForm(request.POST, instance=obj)
        if form.is_valid():
            val = form.save(commit=False)
            val.pedido = obj.pedido       # aseguramos que no cambie
            val.usuario = obj.usuario     # aseguramos que no cambie
            val.save()
            return redirect("core:Valoracion_detail", pk=val.pk)
    else:
        form = ValoracionForm(instance=obj)

    return render(
        request,
        "Valoracion/form.html",
        {"form": form, "mode": "edit", "valoracion": obj}
    )

@require_http_methods(["GET", "POST"])
def Valoracion_delete(request, pk):
    obj = get_object_or_404(Valoracion, pk=pk)

    if request.method == "POST":
        obj.delete()
        return redirect("core:home")

    return render(
        request,
        "Valoracion/confirm_delete.html",
        {"valoracion": obj}
    )