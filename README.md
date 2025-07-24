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

<img width="1892" height="1006" alt="Screenshot 2025-07-24 004249" src="https://github.com/user-attachments/assets/010347ba-7fad-4ea3-9e91-e1c9d7568b45" />


<img width="1618" height="990" alt="Screenshot 2025-07-24 004347" src="https://github.com/user-attachments/assets/fff50602-94eb-4755-9da3-1cad981d8588" />



<img width="1685" height="895" alt="Screenshot 2025-07-24 071303" src="https://github.com/user-attachments/assets/61005c19-50af-4b7e-9a60-f197d51c585a" />


<img width="1792" height="977" alt="Screenshot 2025-07-24 072643" src="https://github.com/user-attachments/assets/3bf6d21c-fcb6-4a3c-86b2-025cf7500f52" />


<img width="1867" height="962" alt="Screenshot 2025-07-24 072832" src="https://github.com/user-attachments/assets/98a3c378-41e5-45af-9ac2-bdfd1a30518f" />
