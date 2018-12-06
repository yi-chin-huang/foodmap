from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import admin
from django.conf import settings

class FoodEvent(models.Model):
	place = models.CharField(max_length=64)
	resource = models.CharField(max_length=64)
	description = models.CharField(max_length=128)
	amount = models.IntegerField(default = 0)
	pai_amount = models.IntegerField(default = 0)
	time = models.DateTimeField(default=datetime.now, blank=True)
	lon = models.FloatField(default = 25.017350,blank = True)
	lat = models.FloatField(default = 121.539794,blank = True)
	provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = False, related_name = "provider")

	def __str__(self):
		return self.resource + "@" + self.place 


class TakeFood(models.Model):
	taker = models.ForeignKey(User, on_delete=models.CASCADE, blank = False)
	food = models.ForeignKey(FoodEvent, on_delete=models.CASCADE,default=1)
	exp_time = models.DateTimeField(default=datetime.now, blank=True)
	rating = models.IntegerField(default = 0) # late: -1 points per 5 mins

	def __str__(self):
		return self.taker + "will take "+ self.food + " at " + self.time

 