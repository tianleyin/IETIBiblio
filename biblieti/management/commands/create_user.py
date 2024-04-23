from django.contrib.auth.models import User

user = User.objects.create_user("isaac", "ifuriomartin.cf@iesesteveterradas.cat", "isaac123")
user.save()