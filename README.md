# User Login API with Email and OTP Authentication

A secure Django REST API for user authentication using email and one-time passwords (OTP).

## Features

- User registration with email validation
- OTP generation and email delivery (console output in development)
- OTP verification with JWT token generation
- Rate limiting for OTP requests
- Docker support

## Prerequisites

- Python 3.9+
- Docker (optional)
- SQLite
## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Pawan-Mario/Login_with_OTP.git
cd user_otp_auth

**2. Set up virtual environment (recommended)**
python -m venv venv
./venv/bin/activate  # On Windows: venv\Scripts\activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Run migrations**
python manage.py migrate

**5. Development Server**
python manage.py runserver

**Docker Setup**
Build the Docker image:

docker build -t user_otp_auth .
Run the container:

docker run -p 8000:8000 user_otp_auth

**API Endpoints
1. Register User**
URL: /api/register/

**2. Request OTP**
URL: /api/request-otp/

**3. Verify OTP**
URL: /api/verify-otp/


