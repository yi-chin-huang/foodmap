# Generated by Django 2.0.9 on 2018-12-27 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodevent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='name',
            new_name='place',
        ),
    ]
