from django.db import models
from django.utils import timezone


class Post(models.Model):
# Create your models here.
	text = models.TextField()
	def publish(self):
		self.save()
	def __str__(self):
		return self.text