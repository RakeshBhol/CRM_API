from rest_framework import generics
from .models import Stock
from .serializers import StockSerializer
from rest_framework.permissions import IsAuthenticated

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]

class StockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]