from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
# from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from .models import User, OTP
from .serializers import (
    UserRegistrationSerializer,
    OTPRequestSerializer,
    OTPVerificationSerializer
)
from .utils import generate_jwt_token, send_otp_email
from rest_framework.throttling import AnonRateThrottle

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user, created = User.objects.get_or_create(email=email)
            if not created and user.is_verified:
                return Response(
                    {"message": "User already registered and verified."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            return Response(
                {"message": "Registration successful. Please verify your email."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPRequestView(APIView):
    # @method_decorator(ratelimit(key='ip', rate='30/s'))
    throttle_classes = [AnonRateThrottle]
    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(
                    {"message": "Email not registered. Please register first."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            otp = OTP.create_otp(user)
            send_otp_email(email, otp.code)
            
            return Response(
                {"message": "OTP sent to your email.", "email": email, "otp": otp.code},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_code = serializer.validated_data['otp']
            
            try:
                user = User.objects.get(email=email)
                otp = OTP.objects.filter(user=user, code=otp_code).latest('created_at')
                
                if not otp.is_valid():
                    return Response(
                        {"message": "OTP has expired. Please request a new one."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                user.is_verified = True
                user.save()
                
                token = generate_jwt_token(user.id)
                
                otp.delete()
                
                return Response({
                    "message": "Login successful.",
                    "token": token
                }, status=status.HTTP_200_OK)
                
            except User.DoesNotExist:
                return Response(
                    {"message": "User not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            except OTP.DoesNotExist:
                return Response(
                    {"message": "Invalid OTP."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)