from django.contrib.auth import get_user_model

# Obtén el modelo de usuario personalizado
User = get_user_model()

# Crea un usuario utilizando el modelo personalizado
user = User.objects.create_user("isaac", "ifuriomartin.cf@iesesteveterradas.cat", "isaac123")
user.save()
