# Generated by Django 5.0.4 on 2024-04-24 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblieti', '0007_remove_user_ieti_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='user_mail',
        ),
    ]
