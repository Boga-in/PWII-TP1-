from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mensajes/',include('mensajes.urls',namespace='mensajes'))
]