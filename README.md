LLM-Powered Chatbot with FastAPI and SQL Integration
Project Description

This project is a full-stack AI-powered chatbot built using Large Language Models (LLMs), FastAPI, and a SQL database for persistent data storage. The chatbot can handle natural language queries, interact with users in real-time, and store/retrieve relevant data from the backend database.

It demonstrates end-to-end integration of an AI model with a web frontend and a relational database, making it ideal for learning modern AI application deployment and backend development.


Features
AI Chatbot: Powered by LLMs for natural language understanding and response generation.
FastAPI Backend: Handles API requests, serves the chatbot, and connects to the database.
SQL Integration: Stores user messages, chat history, and other structured data for persistent storage.
Frontend Interface: Responsive web interface for interacting with the chatbot.
Extensible Architecture: Easily swap out the LLM, database, or frontend for customization.
Secure and Configurable: Uses .env files and environment variables for sensitive configuration.

Project Structure
backend/           # FastAPI backend code
  └─ app/          # API routes, DB connection, chatbot logic
frontend/          # Web interface (HTML, JS, Node.js)
myenv/             # Local Python virtual environment (ignored in Git)
database.db        # SQLite database (ignored in Git)
requirements.txt   # Python dependencies
.gitignore         # Files/folders to ignore in Git


Technologies Used

Python 3.10+ – Backend logic and LLM integration
FastAPI – Web API framework for serving requests
SQLite / SQLAlchemy – Database storage and management
HTML, CSS, JavaScript, Node.js, Vite – Frontend interface
Large Language Model (LLM) – NLP model for chatbot responses

Setup Instructions

Clone the repository
git clone https://github.com/DEEPSEN1998/LLM-Powered-Chatbot-with-FastAPI-and-SQL-Integration.git
cd "LLM-Powered Chatbot with FastAPI and SQL Integration"
Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate      # Windows
source myenv/bin/activate   # Mac/Linux
Install dependencies
pip install -r requirements.txt
Run FastAPI backend
uvicorn backend.app.main:app --reload
Open frontend
cd frontend
npm install
npm run dev


Access the chatbot

Open the web browser at http://localhost:5173 (Vite dev server)
