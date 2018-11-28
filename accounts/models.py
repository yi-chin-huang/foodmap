from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# class UserProfile(models.Model):
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'pds'E)
# 	userscore = models.IntegerField(default='0')

# 	def __str__(self):
#         return self.title