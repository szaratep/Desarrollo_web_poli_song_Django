from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request,"home.html",{"title": "Hola Django!"})

def api_ping(request):
    return JsonResponse({"ok": True, "message": "pong"})

def api_echo(request):
    msg = request.GET.get("msg")
    if not msg:
        return JsonResponse({"error": "falta 'msg'."}, status= 400)
    return JsonResponse({"echo": msg, "length": len(msg)}, status= 200)
