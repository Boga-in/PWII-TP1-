from django.urls import path
from .views import ver_mensajes, index, filtrar_mensajes

app_name = 'mensajes'

urlpatterns = [
    path('', index,name='index'),
    path('recibidos/', ver_mensajes, name='ver_mensajes'),
    path('filtrar/', filtrar_mensajes, name='filtrar_mensajes'),
]