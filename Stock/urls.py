from django.urls import path
from .views import StockListCreateView, StockRetrieveUpdateDestroyView

urlpatterns = [
    path('stocks/', StockListCreateView.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroyView.as_view(), name='stock-detail'),
]