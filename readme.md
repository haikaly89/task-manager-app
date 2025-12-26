# Task Manager

A simple and efficient **Task Management** application built with **React** (Frontend) and **FastAPI** (Backend). This application allows users to register, log in, and manage their personal tasks securely.

## Tech Stack

### **Frontend:**
* **React** (Vite)
* **Tailwind CSS** (Styling)
* **Axios** (API Integration)

### **Backend:**
* **Python** (FastAPI Framework)
* **SQLAlchemy** (ORM)
* **MySQL** (Database)
* **JWT** (JSON Web Token for Authentication)

## Features

*  **User Authentication:** Secure Register and Login system.
*  **JWT Authorization:** Protected routes (Dashboard only accessible with a valid token).
*  **Create Tasks:** Users can add new tasks with titles and descriptions.
*  **View Tasks:** Personalized dashboard showing only the logged-in user's tasks.
*  **Responsive Design:** Clean UI built with Tailwind CSS.

---

##  Installation & Setup

Follow these steps to run the project locally.

###  Prerequisites
* **Node.js & npm** installed.
* **Python** installed.
* **XAMPP** (or any MySQL server) running.

### 1. Database Setup
1.  Open **XAMPP** and start **MySQL**.
2.  Create a new database named: `task_manager`.

### 2. Backend Setup (Server)

Open a terminal and navigate to the server folder:

```bash
cd server
```
Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic "python-jose[cryptography]" "passlib[bcrypt]"
```

Run the server:
```bash
uvicorn main:app --reload
```

The server will run on: `http://127.0.0.1:8000`

### 3. Frontend Setup (Client)L

Open a terminal and navigate to the server folder:

```bash
cd client
```
Install dependencies:
```bash
npm install
```

Run the application:
```bash
npm run dev
```
The server will run on: `http://localhost:5173`


**Screenshots:**

<img width="635" height="557" alt="image" src="https://github.com/user-attachments/assets/b55c16e9-d384-47c5-877e-4a733590f0bb" />
