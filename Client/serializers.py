from rest_framework import serializers
from .models import Client

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email','phone']