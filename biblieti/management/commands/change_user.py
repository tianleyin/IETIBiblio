# en la ruta_de_tu_proyecto/tu_aplicacion/management/commands/modify_user.py

from django.core.management.base import BaseCommand
from biblieti.models import User_ieti
from django.utils import timezone

class Command(BaseCommand):
    help = 'Modifica un usuario existente'

    def handle(self, *args, **options):
        # Recuperar el usuario de la base de datos
        user = User_ieti.objects.get(pk=1)  # Suponiendo que el ID del usuario es 1

        # Modificar los valores del usuario
        user.name = "Tianle"
        user.mail = "tianleyin8888@gmail.com"
        user.password = "1234"  # Establecer la contraseña hasheada
        user.role = "Student"
        user.date_of_birth = timezone.now()  # Asignar la fecha actual
        user.school = ""  # Asignar el valor deseado para la escuela
        user.cycle = ""  # Asignar el valor deseado para el ciclo
        user.picture = None  # Asignar None si no hay imagen o la nueva imagen

        # Guardar los cambios en la base de datos
        user.save()

        self.stdout.write(self.style.SUCCESS('Usuario modificado exitosamente.'))
