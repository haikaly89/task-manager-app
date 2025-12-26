Task Manager
A simple, secure, and efficient Task Management application built with React and FastAPI. This project demonstrates a complete full-stack workflow including authentication, database management, and CRUD operations.

Tech Stack
Frontend:
React (Vite): Fast and modern frontend framework.
Tailwind CSS: Utility-first CSS framework for styling.
Axios: For handling HTTP requests.
Backend:
Python (FastAPI): High-performance backend framework.
SQLAlchemy: ORM for database interaction.
MySQL: Relational database management system.
JWT (JSON Web Token): Secure authentication mechanism.

Features
User Registration & Login: Secure authentication system using hashed passwords and JWT.
Protected Routes: Only authenticated users can access the dashboard.
Personalized Dashboard: Users can only see and manage their own tasks.
Create Tasks: Add new tasks with titles and descriptions.
View Task List: Real-time fetching of tasks from the database.

Installation & Setup
Follow these steps to run the project locally on your machine.
Prerequisites
Node.js & npm installed.
Python installed.
XAMPP (or any MySQL Server) running.

1. Database Setup
Open your MySQL client (DBeaver, phpMyAdmin, etc.).
Create a new database named: task_manager
No need to create tables manually, the backend will do it automatically.

2. Backend Setup (Server)
Open a terminal and navigate to the server folder:
cd server
Create and activate a virtual environment:

# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate


Install required dependencies:

pip install fastapi uvicorn sqlalchemy pymysql pydantic python-jose[cryptography] passlib[bcrypt]


Run the server:
uvicorn main:app --reload

The server will start at http://127.0.0.1:8000

3. Frontend Setup (Client)
Open a new terminal and navigate to the client folder:
cd client
Install Node.js dependencies:
npm install
Run the React application:
npm run dev

The app will be accessible at http://localhost:5173

📚 API Documentation
FastAPI provides automatic interactive documentation. Once the backend is running, visit:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

🤝 Contributing
Fork the repository.
Create a new branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.
