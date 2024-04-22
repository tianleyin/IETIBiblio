# Generated by Django 5.0.4 on 2024-04-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblieti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='imgs/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='imgs/'),
        ),
    ]