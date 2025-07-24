import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def send_otp_email(email, otp_code):
    print(f"Mock email sent to {email} with OTP: {otp_code}")