# Generated by Django 2.2 on 2020-09-17 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20200917_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='image4',
            new_name='image',
        ),
    ]
