# Generated by Django 2.2 on 2020-09-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20200917_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='image',
        ),
        migrations.AddField(
            model_name='client',
            name='image4',
            field=models.ImageField(default='', null=True, upload_to='uploads/'),
        ),
    ]
