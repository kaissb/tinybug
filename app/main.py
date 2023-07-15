# app/main.py

from app.database.database import db
from app.database.models import Issue
from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
templates = Jinja2Templates(directory="templates")
app = FastAPI()

# Get the API key from the environment variable
server_api_key = os.getenv("API_KEY")
user = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")


@app.get("/")
def read_root():
    return {"This is": "TinyBug!"}


@app.get("/issues", response_class=HTMLResponse)
def get_issues(request: Request):
    issues = db.all()
    return templates.TemplateResponse(
        "issues.html", {"request": request, "issues": issues}
    )


@app.post("/issues")
def report_issue(issue: Issue, request: Request, api_key: str = Header(...)):
    if server_api_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    issue_id = len(db) + 1
    # Convert the timestamp to string
    timestamp_str = issue.timestamp.isoformat()
    db.insert(
        {
            "id": issue_id,
            "message": issue.message,
            "timestamp": timestamp_str,
            "stack_trace": issue.stack_trace,
        }
    )
    return {"message": "Issue reported successfully!", "issue_id": issue_id}


@app.post("/login")
def login(request: Request, username: str, password: str):
    if username == user and password == pwd:
        # Successful login, redirect to the protected page
        return RedirectResponse(url="/protected")
    else:
        # Invalid credentials, display error message
        return templates.TemplateResponse(
            "login.html", {"request": request, "error_message": "Invalid credentials"}
        )


@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
