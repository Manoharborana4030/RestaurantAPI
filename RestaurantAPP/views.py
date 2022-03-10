from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Sum


class restaurant(APIView):
	def get(self,request):
		obj = Restaurant.objects.all()
		serializer = RestaurantSerializer(obj,many=True)
		return Response(serializer.data)

class category(APIView):
	def get(Self,request):
		obj = Category.objects.all()
		serializer = CategorySerializer(obj,may=True)
		return Response(serializer.data)