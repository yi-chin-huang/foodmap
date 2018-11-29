from django.db import models
from django.utils.timezone import now
from datetime import datetime

from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

class FoodEvent(models.Model):
	place = models.CharField(max_length=64)
	resource = models.CharField(max_length=64)
	description = models.CharField(max_length=128)
	amount = models.IntegerField(default = 0)
	time = models.DateTimeField(default=datetime.now, blank=True)


	def __str__(self):
		return self.place + " " + self.resource

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }




# class CityForm(forms.ModelForm):

#     class Meta:
#         model = City
#         fields = ("coordinates", "city_hall")
#         widgets = {
#             'coordinates': GooglePointFieldWidget,
#             'city_hall': GoogleStaticOverlayMapWidget,
#         }