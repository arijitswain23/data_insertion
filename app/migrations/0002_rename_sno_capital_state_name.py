# Generated by Django 4.2.6 on 2023-12-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capital',
            old_name='Sno',
            new_name='State_name',
        ),
    ]
