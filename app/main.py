# app/main.py

from app.database.database import db
from app.database.models import Issue
from fastapi import FastAPI, Request, Header, HTTPException, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.database.database import collection
from dotenv import load_dotenv
import os, secrets

load_dotenv()  # Load environment variables from .env file
templates = Jinja2Templates(directory="templates")
app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Get the API key from the environment variable
key = os.getenv("SESSION_SECRET_KEY")
server_api_key = os.getenv("API_KEY")
pwd = os.getenv("PASSWORD")


def verify_password(password: str):
    valid_password = secrets.compare_digest(password, pwd)
    return valid_password


@app.get("/")
def read_root():
    return {"This is": "TinyBug!"}


@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request, error_message: str = ""):
    return templates.TemplateResponse(
        "login.html", {"request": request, "error_message": error_message}
    )


@app.get("/issues", response_class=HTMLResponse)
def issues_get_redirect(request: Request):
    return templates.TemplateResponse(
        "login.html", {"request": request, "error_message": ""}
    )


@app.post("/issues", response_class=HTMLResponse)
async def get_issues(request: Request, password: str = Form(...), page: int = Form(1)):
    if not verify_password(password):
        return templates.TemplateResponse(
            "login.html", {"request": request, "error_message": "Invalid password."}
        )
    else:
        per_page = 10  # Change as needed
        start = (page - 1) * per_page
        issues = list(collection.find().skip(start).limit(per_page))
        total_issues = collection.count_documents({})
        return templates.TemplateResponse(
            "issues.html", {"request": request, "issues": issues, "page": page, "total_pages": total_issues // per_page + (1 if total_issues % per_page > 0 else 0)}
        )


@app.post("/report_issue")
def report_issue(issue: Issue, request: Request, api_key: str = Header(...)):
    if server_api_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    issue_data = issue.dict()
    issue_data["timestamp"] = issue_data["timestamp"].isoformat()

    inserted_issue = collection.insert_one(issue_data)

    return {
        "message": "Issue reported successfully!",
        "issue_id": str(inserted_issue.inserted_id),
    }
