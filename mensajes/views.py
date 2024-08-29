from django.shortcuts import render
from .models import Mensaje

def ver_mensajes(request):
    mensajes_recibidos = Mensaje.objects.all().order_by('fecha_hora')
    return render(request, 'mensajes/recibidos.html', {'mensajes': mensajes_recibidos})

def index(request):
    return render(request, 'mensajes/index.html')

def filtrar_mensajes(request):
    destinatarios = Mensaje.objects.values_list('destinatario', flat=True).distinct()
    mensajes_filtrados = None

    if request.method == 'POST':
        destinatario_seleccionado = request.POST.get('destinatario')
        if destinatario_seleccionado:
            mensajes_filtrados = Mensaje.filtrar_por_destinatario(destinatario_seleccionado)

    return render(request, 'mensajes/filtrar.html', {
        'destinatarios': destinatarios,
        'mensajes': mensajes_filtrados,
    })
