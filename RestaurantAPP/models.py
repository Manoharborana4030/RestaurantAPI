from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	city = models.CharField(max_length=20)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Category(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

	def __str__(self):
		return self.name+self.restaurant.name

class Item(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	price = models.IntegerField()
	available = models.BooleanField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
