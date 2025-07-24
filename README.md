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



## OutPut

![RegisterUser](https://github.com/user-attachments/assets/be03db00-9b97-4d93-babf-88e493333437)

<img width="1618" height="990" alt="Screenshot 2025-07-24 004347" src="https://github.com/user-attachments/assets/2fdf97a2-5540-4c04-90a5-81044c8af586" />



<img width="1685" height="895" alt="Screenshot 2025-07-24 071303" src="https://github.com/user-attachments/assets/58d3c49a-7483-4cd5-9d06-25475e149a90" />

<img width="1792" height="977" alt="Screenshot 2025-07-24 072643" src="https://github.com/user-attachments/assets/390d276d-7026-448d-ab6d-4b74c7fe1a84" />

<img width="1867" height="962" alt="Screenshot 2025-07-24 072832" src="https://github.com/user-attachments/assets/16ed65d8-9729-4679-a68f-2d7b4670bfa8" />



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

