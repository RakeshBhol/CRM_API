from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'symbol', 'price', 'quantity', 'owner', 'client', 'created_at', 'updated_at']