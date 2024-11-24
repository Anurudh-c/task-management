
# Project Setup and Running Documentation

## Overview
This documentation explains how to set up and run the backend and frontend of the project locally after cloning it from GitHub. 
It covers installing dependencies, configuring the environment, and running the project.

## Backend Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo/backend
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
     ```bash
     venv\Scripts\activate
     ```
 
4. **Install Backend Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   - The backend server will run on `http://127.0.0.1:8000`.

## Frontend Setup

1. **Navigate to the Frontend Directory:**
   ```bash
   cd ../frontend
   ```

2. **Install Frontend Dependencies:**
   ```bash
   npm install
   ```
3. **Run the Development Server:**
   ```bash
   npm start
   ```
   - The frontend will run on `http://localhost:3000`.
