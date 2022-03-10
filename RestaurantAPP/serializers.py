from rest_framework import serializers
from .models import *
from django.db.models import Sum


class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = 'Restaurant'
		field = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = 'Category'
		field = '__all__'

