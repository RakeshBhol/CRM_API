from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined']

from rest_framework import serializers

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()