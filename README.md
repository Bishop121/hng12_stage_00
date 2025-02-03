# Public API (HNG12 Stage 0 Task)

## Project Overview
This is a simple public API built with Flask that returns the following information in JSON format:
- Your registered email address (used to register on the HNG12 Slack workspace).
- The current datetime as an ISO 8601 formatted timestamp.
- The GitHub URL of the project's codebase.

## Technology Stack
- **Programming Language**: Python
- **Framework**: Flask
- **Deployment**: Any publicly accessible platform (e.g., Vercel, PythonAnywhere, Heroku, etc.)
- **CORS Handling**: Implemented using `flask-cors`

## API Endpoint
### **GET /**
#### **Response Format**
```json
{
  "email": "obidikeemmanuel@outlook.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Bishop121/your-repo"
}
```

## Setup Instructions
### **1. Clone the repository**
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### **2. Create a virtual environment (optional but recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run the Flask app locally**
```sh
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

## Deployment Instructions
### **Deploying on Heroku**
1. Install Heroku CLI
2. Create a `Procfile` with the following content:
   ```
   web: gunicorn app:app
   ```
3. Login to Heroku and create an app:
   ```sh
   heroku login
   heroku create your-app-name
   ```
4. Push the code:
   ```sh
   git add .
   git commit -m "Deploy API"
   git push heroku main
   ```
5. Your API will be live at `https://your-app-name.herokuapp.com/`

## Useful Links
- **Python Developers**: [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)
- **GitHub Repository**: [https://github.com/yourusername/your-repo](https://github.com/yourusername/your-repo)

---
**Author**: Obidike Chukwuebuka 


