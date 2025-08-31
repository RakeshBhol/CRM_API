from rest_framework import serializers
from .models import CustomUser, Role

class CustomUserSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Role.objects.all())
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'roles' ,'is_active', 'is_staff', 'date_joined']


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()