from rest_framework import serializers
from .models import *
from django.db.models import Sum

class IteamSSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'