# Generated by Django 5.0.6 on 2024-07-02 18:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DatosExtras',
            new_name='DatosExtra',
        ),
    ]
