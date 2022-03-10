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