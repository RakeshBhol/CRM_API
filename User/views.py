from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .serializers import ForgotPasswordSerializer


# User Views
class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

# Login and Logout Views
class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'message': 'Please log in to access this endpoint.'}, status=status.HTTP_200_OK)
    def post(self, request):
        if request.user.is_authenticated:
            return Response({'message': 'Already authenticated'}, status=status.HTTP_200_OK)
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    

# Forgot Password View
class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://localhost:8000/reset-password/{uid}/{token}/"

            # Send email (configure EMAIL settings in settings.py)
            send_mail(
                'Password Reset',
                f'Click the link to reset your password: {reset_link}',
                'noreply@example.com',
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset link sent to your email.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)