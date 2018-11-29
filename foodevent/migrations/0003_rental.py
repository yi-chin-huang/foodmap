# Generated by Django 2.0.9 on 2018-11-26 16:36

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('foodevent', '0002_foodevent_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
    ]
