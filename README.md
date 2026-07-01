PrimeTrade Backend
A full-stack task management application built using FastAPI, MongoDB, JWT Authentication, and HTML/CSS/JavaScript.

Features
User Registration
User Login
Password Hashing using bcrypt
JWT Authentication
Protected Dashboard
Create Task
View Tasks
Update Task
Delete Task
MongoDB Atlas Integration
RESTful APIs
Simple Frontend
Tech Stack
Backend
FastAPI
Python
MongoDB Atlas
PyMongo
Passlib (bcrypt)
Python-JOSE (JWT)
Uvicorn
Frontend
HTML
CSS
JavaScript
Project Structure
PrimeTrade-Backend
│
├── app
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── task_model.py
│
├── frontend
│   ├── background.jpg
│   ├── dashboard.html
│   ├── index.html
│   ├── login.html
│   ├── script.js
│   └── style.css
│
├── README.md
├── requirements.txt
└── .gitignore
Installation
Clone the repository
git clone https://github.com/padmavathiThadi/PrimeTrade-Backend.git
Create a virtual environment
python -m venv venv
Activate the virtual environment
Windows:

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Start the server
uvicorn app.main:app --reload
Open Swagger UI
http://127.0.0.1:8000/docs
API Endpoints
POST /register
POST /login
GET /dashboard
POST /tasks
GET /tasks
PUT /tasks/{task_id}
DELETE /tasks/{task_id}
Author
Thadi Padmavathi

GitHub: https://github.com/padmavathiThadi

