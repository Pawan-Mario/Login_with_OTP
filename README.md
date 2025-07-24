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

<img width="1892" height="1006" alt="Image" src="https://github.com/user-attachments/assets/2f4ea25e-db43-4397-80e7-0d772cd79ea5" />

<img width="1618" height="990" alt="Screenshot 2025-07-24 004347" src="https://github.com/user-attachments/assets/44922f90-1a6a-472a-8c4e-7630034981f6" />



<img width="1685" height="895" alt="Screenshot 2025-07-24 071303" src="https://github.com/user-attachments/assets/07dec524-70fb-483c-bd65-5859667d8171" />

<img width="1792" height="977" alt="Screenshot 2025-07-24 072643" src="https://github.com/user-attachments/assets/2d24f0bc-86c1-429d-85d9-2b814ad8b19d" />


<img width="1867" height="962" alt="Screenshot 2025-07-24 072832" src="https://github.com/user-attachments/assets/484512bd-941a-40cb-ac2a-7c8d91c54241" />

