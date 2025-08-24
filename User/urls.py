from django.urls import path
from .views import (
    CustomUserListCreateView,
    CustomUserRetrieveUpdateDestroyView,
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]