from django.shortcuts import render
from .models import Mensaje

# Create your views here.
def ver_mensajes(request):
    mensajes_recibidos = Mensaje.objects.all().order_by('fecha_hora')

    return render(request, 'mensajes/recibidos.html',{'mensajes' : mensajes_recibidos})

def index(request):
    return render(request,'mensajes/index.html')