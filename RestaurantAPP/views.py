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



def home(request):
    return render(request,'app/home.html')

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
  
class IteamData(APIView):
    serializer_class=IteamSSerializer
    def get(self,request):
        iteam=Item.objects.all()
        serializer=IteamSSerializer(iteam,many=True)
        return Response(serializer.data)
       
    def post(self,request):
        serializer=IteamSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Inserted'})
        return(serializer.errors)
