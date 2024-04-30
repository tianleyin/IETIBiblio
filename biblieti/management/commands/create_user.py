from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Obtén el modelo de usuario personalizado
        User = get_user_model()

        # Crea un usuario utilizando el modelo personalizado
        user = User.objects.create_user("isaac", "ifuriomartin.cf@iesesteveterradas.cat", "Isaac123?")
        user.save()
