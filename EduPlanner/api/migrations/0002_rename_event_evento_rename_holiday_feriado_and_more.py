# Generated by Django 5.1.3 on 2024-11-22 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Evento',
        ),
        migrations.RenameModel(
            old_name='Holiday',
            new_name='Feriado',
        ),
        migrations.RenameModel(
            old_name='Notification',
            new_name='Notificacion',
        ),
        migrations.RenameModel(
            old_name='Review',
            new_name='Revision',
        ),
    ]
