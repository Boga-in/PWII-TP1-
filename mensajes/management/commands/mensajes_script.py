
from django.core.management.base import BaseCommand
from mensajes.models import Mensaje

class Command(BaseCommand):
    help = 'Poblar la base de datos'

    def handle(self, *args, **options):
        # Lógica para poblar la base de datos
        obj = Mensaje(remitente=f'Maria',destinatario=f'Mario',texto='Buenos dias, Necesito esas copias')
        obj.save()
        obj = Mensaje(remitente=f'Jose',destinatario=f'Jose',texto='Que tal! El proyecto esta en proceso')
        obj.save()
        obj = Mensaje(remitente=f'Pedro',destinatario=f'Maria',texto='Ya no se me ocurre nada y es el tercer mensaje')
        obj.save()
        obj = Mensaje(remitente=f'Pedro',destinatario=f'Mario',texto='Buenas tardes, es un hermoso clima el de hoy')
        obj.save()
        obj = Mensaje(remitente=f'Jose',destinatario=f'Maria',texto='Le presento este correo para invitarla al baile')
        obj.save()
        obj = Mensaje(remitente=f'Mario',destinatario=f'Jose',texto='Si, Muchas gracias')
        obj.save()
        
        self.stdout.write(self.style.SUCCESS('Completado.'))